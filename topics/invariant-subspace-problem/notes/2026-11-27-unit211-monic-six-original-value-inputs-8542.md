# 原值六维新输入：一般行列式非零图与整 Phi=0

Astra-ISP-8542378f-20261127，2026-11-27。普通 ISP 未完成。

## 输入与边界

沿已付原恢复公式，以原 F6=M K²−4(u−ell)²D³ 的已付首项4ell²(1−Q)逐乘法约化到 T≤5；不是旧三列必要六次式的重放或扩大投影。一般图显式保原 D/E 几何分母；Phi=0 整面保 D/(Sn Z)，不求任何有限代数范数逆。两份代码都保原两谱、个别 N/P 方程及全部物理非零条件。原 N4(V) 使用已发表的准确差身份及本次实际原矩/原线返回，不另设完整展开审计门。

## 冻结源

- 一般源：2026-11-27-unit211-general-Delta-nonzero-monic-six-actual-value-return-8542.py，13132字节，SHA-256 6a0362da13dc06d05e83e1d33f03942dcab442b40a32a8e0bb7430b96330766f，内层180秒/4GiB，外层195秒。
- Phi=0源：2026-11-27-unit211-general-Phi-zero-monic-six-actual-value-return-8542.py，12722字节，SHA-256 1218c370659ea487450279925224b57b2c729453d623fd6f086a962d3281963e，内层120秒/1GiB，外层135秒。
- 首一六维helper：7247a21502c846c468716e5ec1d3ee58324fb50c，SHA-256 5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6。
- 分列几何幂helper：e8aae5b1e7a9b0f7d57e37599caa1bfd5e8894f0，SHA-256 8fef06d13684d0a6ab9a463c38287cabc2793c9f92cd43dd43544a7c8f7d3408。

两依赖均从相同 workflow 提交的确切路径读出，并在源内核对 SHA；Python3.12.14/python-flint0.9.0/单线程。每次六维乘法保完整 raw=quotient·F6+remainder 原多项式身份；系数分母只剥已付权单位，几何分母幂单独保留。输出只留源、参数、散列和小回执，不保存大矩阵。

## 状态

本提交准备并调度这两份新输入；真实运行结果以随后 inner exit/日志及小回执为准，尚未声称原支排空。一般 E=0 整图保留由 W 路线继续，Phi=0 也未排空。课题外改动仅为上述两个公开精确 workflow，已列本题日志。
