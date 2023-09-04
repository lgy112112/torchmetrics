# Copyright The Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import namedtuple

import torch

from unittests import BATCH_SIZE, EXTRA_DIM, NUM_BATCHES
from unittests.helpers import seed_all

seed_all(42)


Input = namedtuple("Input", ["preds", "target"])
NUM_CLASSES = 10

# extrinsic input for clustering metrics that requires predicted clustering labels and target clustering labels
_single_target_extrinsic1 = Input(
    preds=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
    target=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
)

_single_target_extrinsic2 = Input(
    preds=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
    target=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
)

_float_inputs_extrinsic = Input(
    preds=torch.rand((NUM_BATCHES, BATCH_SIZE)), target=torch.rand((NUM_BATCHES, BATCH_SIZE))
)

# intrinsic input for clustering metrics that requires only predicted clustering labels and the cluster embeddings
_single_target_intrinsic1 = Input(
    preds=torch.randn(NUM_BATCHES, BATCH_SIZE, EXTRA_DIM),
    target=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
)

_single_target_intrinsic2 = Input(
    preds=torch.randn(NUM_BATCHES, BATCH_SIZE, EXTRA_DIM),
    target=torch.randint(high=NUM_CLASSES, size=(NUM_BATCHES, BATCH_SIZE)),
)