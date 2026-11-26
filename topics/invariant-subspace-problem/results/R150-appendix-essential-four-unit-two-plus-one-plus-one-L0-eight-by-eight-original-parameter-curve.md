# R150 / L0：原低 rho 次数矩阵的参数必要曲线

日期：2026-11-27（台北时间，UTC+8）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：以下原组合和参数必要曲线已证明；一般 L0 尚未排除。** 本条使用原 mean 与 N1 的低 rho 次数乘法行，不重新运行已冻结的 X/Y 大投影。

## 1. 同一个原点与矩阵

沿用 [完整原 L0 已付首项系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-full-original-paid-rho-leading-system.md)。原 P1 的系数 alpha 已付，取同一个 t=-beta/alpha；所有原物理因子及 W/G/K/V 的整边界均有此前证明。记该自含源重新生成的四个原必要多项式为

$$F_E=F_{E_1},\quad F_N=F_{N_1},\quad F_O=F_{E_{B,\mathrm{odd}}},\quad F_B=F_{E_{B,\mathrm{even}}}.$$

它们的 rho 次数分别为 5、5、6、7；这是同一参数点上的原返回，没有另选根或改变 t。按以下次序取八行：

$$F_E,\rho F_E,\rho^2F_E,F_N,\rho F_N,\rho^2F_N,F_O,F_B.$$

在列 $(\rho^7,\rho^6,\ldots,\rho,1)$ 上形成 $8\times8$ 矩阵 $M(\lambda,w)$。每行从系数重建并与原多项式逐项比较。矩阵 SHA-256 为

`96d04a75ba9b00d726bddcd70d7686092aa152bc805972d1eca3882ab5016875`。

## 2. 余子式的原八列回乘

分数自由 Bareiss 的每次多项式商均乘回。逆向只恢复常数坐标的余子式行 $c$，并精确核验

$$cM=(0,\ldots,0,D),\qquad \sum_{i=1}^{8}c_iM_i(\rho)=D(\lambda,w).$$

因此 $D$ 属于上述八个真实原多项式生成的理想。$D$ 的参数次数为 $(86,127)$、共 8534 项，SHA-256 为

`3e9e8cf54336b988f2c96be352eb09aeb9b57787f8718796880199bb1c780a4d`。

这是一条全局多项式身份。中间消元主元只用于求出该身份；结论没有倒置它们，所以主元为零的参数纤维仍保留。

源码逐项剥除已经证明非零的物理/曲线因子，实际核验 $D=UC$ 及 $U$ 全部因子已付。剩余规范多项式满足

$$\boxed{C_{39,53}(\lambda,w)=0}$$

于每个剩余 L0 原点成立。其次数为 $(39,53)$、共 1843 项，SHA-256 为

`6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c`。

这里不声称 C 不可约或该单曲线为空。它须继续与已有 $X_{34,52}$、$Y_{78,95}$ 及同 rho/t 的完整原 P/N 返回一起使用。

## 3. 实际执行与最初实现错误

源：[2026-11-27-unit211-L0-eight-by-eight-original-parameter-curve-8542.py](../notes/2026-11-27-unit211-L0-eight-by-eight-original-parameter-curve-8542.py)，16,065 字节，SHA-256

`26c70e8e45b1e0fb1f24ab6f31b63492748f83855ec460dca40ce0a4c6c456eb`。

无参数；Python 3.12.14、python-flint 0.9.0；180 秒源 alarm、4 GiB 地址空间、190 秒外部硬限。实际退出码 0，墙钟 15.766025 秒，最大 RSS 91,772 KiB；最后源记录 15.676440 秒。stdout 15,842 字节，SHA-256

`06efc5ab90be12af1dcbfe76ddcf172d4d5c2a1b5b1cf9b9129b2f5cb34ef9da`。

[小回执](../notes/2026-11-27-unit211-L0-eight-by-eight-original-parameter-curve-execution-8542.json)包含最终记录、全部限制及失败身份。源保留本次实际运行的可选 scratch 缓存输出路径；复现时须建立该父目录或映射路径，不保存大系数表。

最初逆向行变换程序把中间有理商误当成多项式商，11.116459 秒、RSS 68,604 KiB、exit 1 因 flint `DomainError` 停止。它没有返回原余子式证书。该 15,995 字节精确失败源与回执均冻结；修正程序从最后 Bareiss 主元开始恢复多项式余子式，最终八个原列身份全通过。本条只使用后一个完整返回。

普通 Hilbert ISP、一般 L0 空性和原 Bell 临界幂来源均未在本条完成。
