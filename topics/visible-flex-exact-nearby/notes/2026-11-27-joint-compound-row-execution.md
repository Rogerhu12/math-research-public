# JC 七个完整联合行标量的实际入口

2026-11-27，visible-exact-astra-fb31ed6-20261127。

[证明](../results/R149-supplement-joint-compound-waist-row-error.md)保持原 selected
W、原96 target、原 L4096/N1024 exact DFT。只读取原完整 EH/G0/G1/H1，
新目标为两个 homotopy Jacobian lower、其合法较大 lower、joint composition、
joint Wiener、完整 alias/tail、最终完整 joint row operator upper，共7球。

[实际 manifest](2026-11-27-joint-compound-waist-row-inputs.json) SHA256
`6e63333d01231f53ba1e69e7097a062ad110a49beb62dc08c69759668a35b6f6`，36个当前全件及4个原历史gzip native。
完整旧 RW 的只读准入函数核 W/R31/K48/H、源、执行、发布、fixed Js；原
KAM、DFT、96行误差、PDE残差或旧范数目标均不运行。旧真/假 loss不改写。

[worker](../scripts/fourfold_codazzi_joint_compound_row_public_worker.py)只替换已修
RW引擎的任务标识、七球validator与报告；四native恢复、容量、README检查、
单child和非FF立即pull/rebase/push循环原样复用。原worker完整SHA固定，
新数学由 [owner](../scripts/fourfold_codazzi_joint_compound_row_owner.py)执行。
前三球保存 lower，后四球保存 upper，每个依赖只消费正式保存读回的方向端点。
完整负候选lower也保留，正的全homotopy门只检查保存球的lower。

运行Python3.12.14/python-flint0.9.0、320bits；child240s、单数学120s，
科学文件≤45KB、receipt≤38KB、总publication≤85KB，保原120KB容量余量。
推送独立workflow触发一次；具体run和实际值由真实输出补记，不预造结果。
SC后继只消费此次完整七球，不再重算JC；全P224/TC与真signed矩阵的前置独立。
