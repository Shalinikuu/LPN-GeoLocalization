import gradio as gr
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image
import cv2
import tempfile
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class AdvancedEdgeGeoLPN(nn.Module):
    def __init__(self, embedding_dim=512, partitions=4):
        super(AdvancedEdgeGeoLPN, self).__init__()
        self.partitions = partitions
        mobilenet = models.mobilenet_v3_large(weights=None)
        self.backbone = mobilenet.features
        self.avg_pool = nn.AdaptiveAvgPool2d((partitions, 1))
        self.fcs = nn.ModuleList([nn.Linear(960, embedding_dim) for _ in range(partitions)])

    def forward(self, x):
        x = self.backbone(x)
        x = self.avg_pool(x)
        part_features = []
        for i in range(self.partitions):
            part = x[:, :, i, 0]
            feat = self.fcs[i](part)
            feat = nn.functional.normalize(feat, p=2, dim=1)
            part_features.append(feat)
        out = torch.cat(part_features, dim=1)
        return nn.functional.normalize(out, p=2, dim=1)

# Load model
model = AdvancedEdgeGeoLPN(partitions=4).to(device)
if os.path.exists('AdvancedEdgeGeoLPN_Best.pth'):
    model.load_state_dict(torch.load('AdvancedEdgeGeoLPN_Best.pth', map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(img_pil):
    tensor = transform(img_pil).unsqueeze(0).to(device)
    with torch.no_grad():
        return model(tensor)

def match_images(sat_img_path, uav_img_path):
    if not sat_img_path or not uav_img_path:
        return None, None, "❌ Please upload both images!"
    
    sat_img = Image.open(sat_img_path).convert('RGB')
    uav_img = Image.open(uav_img_path).convert('RGB')
    
    sat_feat = extract_features(sat_img)
    uav_feat = extract_features(uav_img)
    
    score = max(0.0, F.cosine_similarity(uav_feat, sat_feat).item() * 100)
    result_text = f"🎉 Match Confidence Score: {score:.2f}%"
    return uav_img, sat_img, result_text

def match_video(sat_img_path, uav_vid_path):
    if not sat_img_path or not uav_vid_path:
        return None, None, "❌ Please upload both the satellite image and UAV video!"
        
    sat_img = Image.open(sat_img_path).convert('RGB')
    sat_features = extract_features(sat_img)
    
    cap = cv2.VideoCapture(uav_vid_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = 30.0 if fps == 0 or fps is None else fps
    frame_interval = int(fps)
    
    best_score = -100.0
    best_frame = None
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame_rgb)
            f_feat = extract_features(pil_img)
            score = F.cosine_similarity(f_feat, sat_features).item() * 100
            if score > best_score:
                best_score = score
                best_frame = pil_img
        frame_count += 1
    cap.release()
    
    if best_frame:
        best_score = max(0.0, best_score)
        return best_frame, sat_img, f"🎯 Best Frame Match Score: {best_score:.2f}%"
    return None, None, "❌ Error processing video frames."

# Gradio Web UI Layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚁 Cross-View UAV & Satellite Geo-Localization")
    gr.Markdown("Upload your files directly from your PC to evaluate cross-view matching.")
    
    with gr.Tabs():
        with gr.TabItem("1. UAV Image & Satellite"):
            with gr.Row():
                with gr.Column():
                    sat_in = gr.Image(type="filepath", label="Satellite Image")
                    uav_in = gr.Image(type="filepath", label="UAV Image")
                    btn1 = gr.Button("Run Image Matching 🚀", variant="primary")
                with gr.Column():
                    out_uav = gr.Image(label="UAV View")
                    out_sat = gr.Image(label="Satellite View")
                    out_text1 = gr.Textbox(label="Result")
            btn1.click(match_images, inputs=[sat_in, uav_in], outputs=[out_uav, out_sat, out_text1])
            
        with gr.TabItem("2. UAV Video & Satellite"):
            with gr.Row():
                with gr.Column():
                    sat_in_v = gr.Image(type="filepath", label="Satellite Image")
                    vid_in = gr.Video(label="UAV Video File")
                    btn2 = gr.Button("Process Video & Match 🚀", variant="primary")
                with gr.Column():
                    out_v_frame = gr.Image(label="Best Matching Video Frame")
                    out_v_sat = gr.Image(label="Satellite View")
                    out_text2 = gr.Textbox(label="Result")
            btn2.click(match_video, inputs=[sat_in_v, vid_in], outputs=[out_v_frame, out_v_sat, out_text2])

demo.launch()
