import cv2,json,torch,torchvision,dataclasses
import pytorch_lightning as pl

from enum import Enum
from tqdm.auto import tqdm
from pycocotools import mask as mask_utils
from contextlib import contextmanager
from typing import *

from torch import tensor, Tensor
from torch.utils.data import DataLoader
from torchvision.transforms.functional import to_tensor as im2tensor
from torchvision.models.detection.faster_rcnn import FasterRCNN,FastRCNNPredictor,fasterrcnn_resnet50_fpn
from torchvision.models.detection.mask_rcnn import MaskRCNN,MaskRCNNPredictor,maskrcnn_resnet50_fpn
from torchvision.models.detection.keypoint_rcnn import KeypointRCNN,KeypointRCNNPredictor,keypointrcnn_resnet50_fpn
from pytorch_lightning import LightningModule, Trainer

from fastcore.imports import *
from fastcore.test import *
from fastcore.foundation import *
from fastcore.utils import *

try: import albumentations as A
except ModuleNotFoundError: pass