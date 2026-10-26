import tensorflow as tf
import tf2onnx

# Load your trained model
model = tf.keras.models.load_model("model/model.h5")

# Define input signature (VERY IMPORTANT)
input_signature = (tf.TensorSpec((None, 53), tf.float32, name="input"),)

# Convert model
onnx_model, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=input_signature,
    opset=13
)

# Save ONNX model
with open("model/model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("✅ ONNX model saved successfully")