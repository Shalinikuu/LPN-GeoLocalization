import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image
import cv2
import tempfile
import os

st.set_page_config(page_title="Cross-View UAV Geo-Localization", page_icon="🚁", layout="centered")

st.title("🚁 Cross-View UAV & Satellite Geo-Localization")
st.write("Live deployment app for cross-view matching using your trained PyTorch model.")

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

# Sidebar Menu with 4 Options
st.sidebar.title("Navigation Menu")
menu = st.sidebar.radio(
    "Choose an Option:",
    (
        "1. Upload Satellite & UAV Image",
        "2. Upload Satellite Image & UAV Video",
        "3. Load Images from Dataset",
        "4. Exit"
    )
)

all_image_types = ["jpg", "jpeg", "png", "webp", "bmp", "tif", "tiff", "jfif"]

if menu == "1. Upload Satellite & UAV Image":
    st.subheader("🖼️ Option 1: Satellite & UAV Image Matching")
    
    col1, col2 = st.columns(2)
    with col1:
        sat_file = st.file_uploader("Upload Satellite Image", type=all_image_types, key="opt1_sat")
    with col2:
        uav_file = st.file_uploader("Upload UAV Image", type=all_image_types, key="opt1_uav")
        
    if sat_file and uav_file:
        sat_img = Image.open(sat_file).convert('RGB')
        uav_img = Image.open(uav_file).convert('RGB')
        
        if st.button("Run Image Matching 🚀", type="primary", key="btn1"):
            with st.spinner("Extracting features..."):
                sat_feat = extract_features(sat_img)
                uav_feat = extract_features(uav_img)
                score = max(0.0, F.cosine_similarity(uav_feat, sat_feat).item() * 100)
                
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.image(uav_img, caption="UAV View", use_column_width=True)
            with res_col2:
                st.image(sat_img, caption="Satellite View", use_column_width=True)
                
            st.success(f"🎉 Match Confidence Score: **{score:.2f}%**")

elif menu == "2. Upload Satellite Image & UAV Video":
    st.subheader("🎥 Option 2: Satellite Image & UAV Video Matching")
    
    col1, col2 = st.columns(2)
    with col1:
        sat_file_v = st.file_uploader("Upload Satellite Image", type=all_image_types, key="opt2_sat")
    with col2:
        vid_file = st.file_uploader("Upload UAV Video File", type=["mp4", "avi", "mov", "mkv"], key="opt2_vid")
        
    if sat_file_v and vid_file:
        sat_img = Image.open(sat_file_v).convert('RGB')
        
        if st.button("Process & Show All Extracted Frames 🚀", type="primary", key="btn2"):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
                tmp.write(vid_file.read())
                temp_vid_path = tmp.name
                
            with st.spinner("Extracting frames and evaluating features..."):
                sat_features = extract_features(sat_img)
                cap = cv2.VideoCapture(temp_vid_path)
                fps = cap.get(cv2.CAP_PROP_FPS)
                fps = 30.0 if fps == 0 or fps is None else fps
                frame_interval = int(fps)
                
                extracted_results = []
                frame_count = 0
                
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if frame_count % frame_interval == 0:
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(frame_rgb)
                        f_feat = extract_features(pil_img)
                        score = max(0.0, F.cosine_similarity(f_feat, sat_features).item() * 100)
                        extracted_results.append((pil_img, score, frame_count))
                    frame_count += 1
                cap.release()
                os.unlink(temp_vid_path)
                
            if extracted_results:
                best_frame_data = max(extracted_results, key=lambda x: x[1])
                st.markdown("---")
                st.markdown("### 🏆 Final Best Match Result")
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.image(best_frame_data[0], caption=f"Best Frame (Sec: {best_frame_data[2]//int(fps)})", use_column_width=True)
                with res_col2:
                    st.image(sat_img, caption="Satellite View", use_column_width=True)
                st.success(f"🎯 Highest Match Confidence Score: **{best_frame_data[1]:.2f}%**")
                
                st.markdown("---")
                st.markdown("### 🎞️ All Extracted Video Frames & Scores")
                cols = st.columns(3)
                for idx, (img, score, f_num) in enumerate(extracted_results):
                    with cols[idx % 3]:
                        st.image(img, caption=f"Frame {f_num} | Score: {score:.2f}%", use_column_width=True)
            else:
                st.error("❌ Could not extract frames from the video.")

elif menu == "3. Load Images from Dataset":
    st.subheader("📂 Option 3: Batch Upload & Test Dataset Images")
    st.write("Aap apne dataset se multiple images yahan ek sath select karke upload kar sakte hain aur unhe test kar sakte hain:")
    
    dataset_files = st.file_uploader("Upload Dataset Images", type=all_image_types, accept_multiple_files=True, key="dataset_batch")
    
    if dataset_files:
        image_names = [file.name for file in dataset_files]
        selected_name = st.selectbox("Select an image from your uploaded dataset:", image_names)
        
        # Find the selected file object
        selected_file = next(f for f in dataset_files if f.name == selected_name)
        dataset_img = Image.open(selected_file).convert('RGB')
        
        st.image(dataset_img, caption=selected_name, width=350)
        
        if st.button("Extract Features & Test 🚀", type="primary", key="btn3"):
            feat = extract_features(dataset_img)
            st.success(f"✅ Features successfully extracted for **{selected_name}** using your model!")

elif menu == "4. Exit":
    st.warning("🔒 Session ended. You can close this tab or select another option from the sidebar.")
