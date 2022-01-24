import tensorflow as tf
import torch
import jax

print(
    f"Pytorch CUDA availability: {torch.cuda.is_available()}, num gpus:"
    f" {torch.cuda.device_count()}"
)
print(f"TensorFlow GPU visibility: {tf.config.list_physical_devices('GPU')}")
print(f"JAX GPU visibility: {jax.devices()}")
