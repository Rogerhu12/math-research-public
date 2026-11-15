# R150 附录：删去 29 个已付核方向后的单次模 65521 原秩

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

## 1. 这一次检验的准确对象

[29 个规范真核](R150-appendix-exact-twentynine-normalized-free-kernels-and-seven-direction-complement.md) 给出完整自由像 $(I_{29},0)^T$。因此从原所选 4354 来源中删去前 29 个自由来源列，不改变其有理列像，得到
$$
C_{\rm red}\in\mathbb Z^{4367\times4325}.
$$
这里的删列身份在 $\mathbb Q$ 上已证明；没有预设同一身份在新素数下仍可用。

本次所有矩阵条目都直接来自原 17 式整数系数，再约化模唯一预定素数 $65521$。没有把旧模 31 正常形或行操作系数拿来使用，也没有扫描多个素数。

## 2. 实际完成结果

run 43679903558，step single-prime65521-selected-rank，执行源提交
$778af4df0b40a54a4db5e12a8d79e3d47e1214ed$。

数学时间为 14.919986302000325 秒，status=completed，exitCode=0。完整原矩阵的精确有限域 RREF 给
$$
\boxed{
\operatorname{rank}_{\mathbb F_{65521}}\overline C_{\rm red}=4318,
\qquad
\dim\ker\overline C_{\rm red}=7.
}
$$
程序构造了全部七列核，并在原完整 4367 行上逐项核其乘积为零。

[实际小回执](../notes/r150-infinity-remote-session-789f/43679903558-single-prime65521-selected-rank.json) 保存了来源字典、源码及所有临时文件的哈希。临时完整主回执为 2011 B，SHA256 为
$8cba54164c75f7ccd456c8a37dbc9c65e4712ebabf8b1c2e1ed5b3a819d92aca$。

可复用的实际列 profile 为 41202 B，SHA256
$523d3835e92d9a8747759c6fa5949c5aec1b452e6f78fc76db5a7455e4c5f66b$；
完整原模矩阵为 37774570 B，SHA256
$a9b89935d75f7c56fd8fe7becc142b7c84a7e1164b481170dc6d9790fe6d3fc3$。
这些大数组只作为当前运行的临时后继输入。

## 3. 特征零能与不能推出什么

模素数的非零子式仍在 $\mathbb Q$ 中非零，所以本次给出同一原有理列像的下界 4318。与已付 29 条真核合并，范围仍是
$$
4318\le\operatorname{rank}_{\mathbb Q}C_0\le4325.
$$
本次没有把上界闭合，也没有把七个新有限域核当成真有理核。它只确认在第二个固定素数下原完整秩也是 4318；不由两个素数的相同值宣布有理秩相同。

该真实 profile 可以用于下一步选择原整数的 4318 个独立来源，再从原行中选一个非零单位子块。对剩余七列的精确有理解及全部原输出残差，才会确定其真正特征零核空间。后继若这样使用 profile，模 65521 仅负责原整数选元，不能替代有理系数求解。

源码为 [单次素数检验程序](../notes/2026-11-15-r150-single-prime65521-selected-rank-789f.py)。不因本次未提高下界而继续多素数尝试，也不由本次结果再盲增原模 31 精度。
