
import torch
import torch.distributed as dist
torch.cuda.set_device(0)
dist.init_process_group(backend='nccl')
config_list = [
    "assets/HLLM/HLLM.yaml",
    "assets/overall/LLM_deepspeed.yaml"
]

from config.configurator import Config

cfg = Config(config_list)

print(cfg)

from data import load_data

dataload = load_data(cfg)

from data import bulid_dataloader

train_loader, valid_loader, test_loader = bulid_dataloader(cfg, dataload)

print(dataload)


dist.destroy_process_group()