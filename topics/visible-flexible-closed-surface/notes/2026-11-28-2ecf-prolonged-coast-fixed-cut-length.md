# 准确 coast 保到 .081 的原 cut 余长不足

**已证明的计算包含。**

R264 在实际 Γ95 原 native 零点推导高度、材料角与空间径切，并给强有限曲率+准确同g的条件性排除。该点从 coast 到当前 R205 cut 的必要余长>.73479772988，实际≤.7346745，缺口>.00012322。证明见正式结果。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径。W 内的 ramp/coast master 由 R232/R233 原命令生成。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-prolonged-coast-cut-necessary.py" --scripts "$S" --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --length .081 --output polar-prolonged-coast-081-exclusion.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-prolonged-coast-cut-necessary.py | 9cb881251f2b0a7bfe1c9ad724d9019f4d40775f7dadff01e0db791d92a28b90 |
| polar-prolonged-coast-081-exclusion.json | 6f0b334814e038580231f51ae5b5af16c064c0cd72b24f113036714169408dd6 |
| polar-prolonged-coast-081-exclusion-exit.json | 5d27e355f41bf011b21e9c7752034842e3b82edab3106873111fb3bef22102cf |
| polar-prolonged-coast-081-exclusion.log | 24a0750ee75257cfa39ab1bee8c2b88038a0b35f087769d7c505651f45a3119f |
