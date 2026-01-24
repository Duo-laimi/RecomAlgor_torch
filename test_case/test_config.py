

config_list = [
    "../assets/HLLM/HLLM.yaml",
    "../assets/overall/LLM_deepspeed.yaml"
]

from config.configurator import Config

cfg = Config(config_list)

print(cfg)