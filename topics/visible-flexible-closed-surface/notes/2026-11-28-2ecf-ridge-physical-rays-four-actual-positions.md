# 高弯开发端口规定速率全径线面的四个真实位置步

**数值证据。**

输入采用固定 gap=23/25 的 H65 前缀、R273 的上弯幅 .85、起弯处 .52、真实 cuff 高度 .415 及喉长 .115。全物理 65 径线的几何惩罚解经 Hermite 与 Fourier 定义全表面。G11 零修正初值的 metric / κ / held 分别为 1.488359382、16.95694121、.6493239885。前缀、开发尾及完整帽按 R267/R273；该底和修正的全域曲率与非局部厚度仍待证明。
在固定此输入的同一 g 上，由自身零系数开始，对完整原 4291840 行及同一物理 H² 施加 4 次阻尼正规 CG 内迭代与非线性 Armijo 回溯，得到 4 个接受。独立 G11 每个状态均重新直接求角导及六 jets。

| 自身步 | G10 R² | G10 metric / κ / held | G11 metric / κ / held |
|---:|---:|---|---|
| 1 | 5.600907499 | 0.8923776901 / 17.01707028 / 0.644045158 | 0.88874091 / 17.00880295 / 0.6440364912 |
| 2 | 0.9100766116 | 0.5246952435 / 16.14987814 / 0.6401914479 | 0.5217123687 / 16.46063433 / 0.6401879459 |
| 3 | 0.3802818342 | 0.3433763117 / 16.36282704 / 0.6389173601 | 0.3423157245 / 17.33038417 / 0.6389256479 |
| 4 | 0.2574247733 | 0.356760404 / 18.61256722 / 0.6351450418 | 0.3547190505 / 18.61767726 / 0.635176825 |

第二态的独立 held 仅余 .000187946 的 .64 预算；第三、第四态低于 .64。第三态独立 metric 降至 .34231572 后回升，各接受值仍离 2e−9 目标。不同尾的较软正转线和本线没有共用接受计数。

## 可移植重生

W 含 [R267 新前缀](../results/R267-new-gap-092-full-physical-prefix-metric-and-reach.md)、新 gap 的 G10/G11 源、原正规算子 audit 以及前项高弯实径线的场文件、设计和全观察报告。S 为公开课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raised-physical-ray-position-source.py" --mode prepare --scripts "$S" --parent polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-ridge-rays.npz --design polar-gap092-raised-ridge-rays.json --observation polar-gap092-raised-ridge-full.json --output polar-gap092-physical-ridge-prepared.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raised-physical-ray-position-source.py" --prepared polar-gap092-physical-ridge-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --zero --initial-damping .06 --steps 0 --prefix polar-gap092-physical-ridge-zero
python3 -u "$S/2ecf-polar-physical-ray-streamed-inner-gn.py" --scripts "$S" --prepared polar-gap092-physical-ridge-prepared.json --state polar-gap092-physical-ridge-zero-initial.json --steps 4 --iterations 4 --prefix polar-gap092-physical-ridge-innerGN
python3 -u "$S/2ecf-polar-physical-ray-G11-states.py" --scripts "$S" --prepared polar-gap092-physical-ridge-prepared.json --states polar-gap092-physical-ridge-innerGN-step01-state.json polar-gap092-physical-ridge-innerGN-step02-state.json polar-gap092-physical-ridge-innerGN-step03-state.json polar-gap092-physical-ridge-innerGN-step04-state.json --output polar-gap092-physical-ridge-innerGN-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| polar-gap092-physical-ridge-prepared.json | a3c8d3bb72c0f2eab22041933e8d52515f528af58fb54ebe1224f2012664323e |
| polar-gap092-physical-ridge-zero-initial.json | a43b9f496f59e639939985e29c6eea2775517125af7b0f6b49d07f9e13f08056 |
| polar-gap092-physical-ridge-innerGN-report.json | b332fb43cedcb9731509c2fe95beb467e2083de2a6f3add954f6e9301ef117cb |
| polar-gap092-physical-ridge-innerGN-G11.json | 8f48a41f51a3c61086f704175e7c1bbc10ecd2c2f378db9ecc85ec104b0d5044 |
| polar-gap092-physical-ridge-innerGN-step01-state.json | c975e83ca2a1f9270dbca5458e660c96b09e014afcaba0590ae3f17e1dcc64fd |
| polar-gap092-physical-ridge-innerGN-step02-state.json | 406ef78e6a9d5eb36e367fe7d4067e82d73563f38841210356be27426e28bb7e |
| polar-gap092-physical-ridge-innerGN-step03-state.json | 7acacf8646098e4e1483c223ea3990a4f322228fd8023a3d7337d029de83e3ae |
| polar-gap092-physical-ridge-innerGN-step04-state.json | 4022cca096806990a50bc570a5ebe3392ffdf828e82b3e50c21098cbceebb045 |
| polar-gap092-physical-ridge-compose-exit.json | 0ddd77420a0f6a550854d31597568c2cf0f55ecdb04b8133ab87cd64ca939787 |
| polar-gap092-physical-ridge-compose.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-gap092-physical-ridge-initial-exit.json | 4d09e56e708c7ae36d7cf0edf9bd0e903542dc4acaabfe80c7372b12b84e8b83 |
| polar-gap092-physical-ridge-initial.log | 89fc1f44e7d92895db6c2ad8c614a31bdcce34ffb4b0dc756f039ce7a0fd0ba2 |
| polar-gap092-physical-ridge-innerGN-exit.json | 1c87e3417504695d90e0b23bdc61f146535464e2eae16391e531a909874ef0ac |
| polar-gap092-physical-ridge-innerGN.log | 79728fca2618fcebc0d4ad4f91a9cc8885955a765d6e1fde47653cce96c921af |
| polar-gap092-physical-ridge-innerGN-G11-exit.json | 293538396bcea6c52468b1c2c80e7957268542eac7208113a82748b3eb916df5 |
| polar-gap092-physical-ridge-innerGN-G11.log | 82cdea21b39d6423a2a5cf45791d53e0796910620e71b18bc66455f2cf76a7c6 |
