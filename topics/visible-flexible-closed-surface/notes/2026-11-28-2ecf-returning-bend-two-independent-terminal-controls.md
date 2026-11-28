# 真实开发端口的尖端高度和切向双控制

**准确有理证明。** [R282](../results/R282-returning-developed-ports-with-independent-terminal-tangent-and-height.md) 给出完整参数矩形中两导数的 Jacobian 绝对值 >3/50。全真实盘的主曲率控制、真实大喉、两整帽及原 gap=23/25 全前缀，组合后含所有端部外共法向，全部相位 reach≥.097、held≥.64、δE≥.1609、D≤3.2；留有连接带的四个边。端口角导/径导由真实新开发积分定义。

## 可移植重生

W 是运行目录，S 为公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 "$S/2ecf-polar-returning-port-all-parameter-bounds.py" --port "$S/2ecf-polar-returning-bend-full-ray-surface.py" --output polar-returning-rigorous.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-returning-bend-full-ray-surface.py | 8388526ebdc797836b1109c8d7e2c0e653c5dbab2f7d58fb8d168d4d7d57fbd2 |
| 2ecf-polar-returning-port-all-parameter-bounds.py | 554c16a53207248a42316287a1056bd320e60eab2bfc4b685b656458674b6fde |
| polar-returning-rigorous.json | 27393ac9838ca45664831a67bd0d325793471e46faefe8b4e2c933f6f5fa46a3 |
| polar-returning-rigorous-exit.json | 89337e9988c47e07f4590564dea4782d7a9244b9a9d59e8bd515ffd003ef619c |
| polar-returning-rigorous.log | 7a6482c06feea972d3f41510dba52f1d255929dbb6640691adcd50a428606531 |
