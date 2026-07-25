import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image
import cv2
import tempfile
import os

st.set_page_config(page_title="Cross-View Matching App", page_icon="🚁", layout="centered")

st.title("🚁 Cross-View UAV & Satellite Matcher")
st.write("Upload your satellite image and drone image or video to check the geo-localization match percentage.")

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

@st.cache_resource
def load_trained_model():
    model = AdvancedEdgeGeoLPN(partitions=4).to(device)
    model_path = 'AdvancedEdgeGeoLPN_Best.pth'
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model

model = load_trained_model()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(img):
    img_tensor = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model(img_tensor)
    return features

menu = st.sidebar.selectbox(
    "Choose Mode:",
    (
        "1. Upload UAV Image & Satellite Image",
        "2. Upload UAV Video & Satellite Image",
        "3. Exit"
    )
)

if menu == "1. Upload UAV Image & Satellite Image":
    st.subheader("🖼️ Upload Image & Map")
    sat_file = st.file_uploader("1️⃣ Upload Satellite Image", type=["jpg", "png", "jpeg"])
    uav_file = st.file_uploader("2️⃣ Upload UAV Image", type=["jpg", "png", "jpeg"])
    
    if sat_file and uav_file:
        sat_img = Image.open(sat_file).convert('RGB')
        uav_img = Image.open(uav_file).convert('RGB')
        
        if st.button("Run Matching 🚀", type="primary"):
            sat_feat = extract_features(sat_img)
            uav_feat = extract_features(uav_img)
            score = F.cosine_similarity(uav_feat, sat_feat).item() * 100
            score = max(0.0, score)
            
            col1, col2 = st.columns(2)
            with col1:
                st.image(uav_img, caption="UAV View", use_column_width=True)
            with col2:
                st.image(sat_img, caption="Satellite View", use_column_width=True)
                
            st.success(f"🎉 Match Confidence Score: **{score:.2f}%**")

elif menu == "2. Upload UAV Video & Satellite Image":
    st.subheader("🎥 Upload Video & Map")
    sat_file = st.file_uploader("1️⃣ Upload Satellite Image", type=["jpg", "png", "jpeg"])
    vid_file = st.file_uploader("2️⃣ Upload UAV Video File", type=["mp4", "avi", "mov"])
    
    if sat_file and vid_file:
        sat_img = Image.open(sat_file).convert('RGB')
        
        if st.button("Process Video & Match 🚀", type="primary"):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
                tmp.write(vid_file.read())
                temp_vid_path = tmp.name
                
            with st.spinner("Scanning video frames..."):
                sat_features = extract_features(sat_img)
                cap = cv2.VideoCapture(temp_vid_path)
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
                os.unlink(temp_vid_path)
                
            if best_frame:
                best_score = max(0.0, best_score)
                col1, col2 = st.columns(2)
                with col1:
                    st.image(best_frame, caption="Best Matching Video Frame", use_column_width=True)
                with col2:
                    st.image(sat_img, caption="Satellite View", use_column_width=True)
                st.success(f"🎯 Best Frame Match Score: **{best_score:.2f}%**")

elif menu == "3. Exit":
    st.warning("App closed.")
