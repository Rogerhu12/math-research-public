# R133 补充：同一 w0 的完整帽 Hessian 源实际验收

公开 Actions [43616252389](https://github.com/Rogerhu12/math-research-public/actions/runs/43616252389) 已实际成功：十项门全部通过，完整 1341 个局部源格和 1977 个真实 Hermite 交格均被消费。数学用时 82.080329043 秒，实际 child 返回 0，用时 85.002428839 秒。

## 1. 实际数值及数学对象

固定中心为 ac1 的连续 M32 修补
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
参数仅为仿射偏移零，即固定物理 $\eta_0$ 与原 $\nu$。本次方向是成功 v3 native 中同一个准确 binary64 向量 $w_0$，全部 97 个 orthonormal even 输入槽（包括均值）均保留。使用原完整 257 状态矩阵的同一列 $t=T w_0$。

全部四项源的严格向外圆整上界为：

| 源范数 | 上界 |
| --- | ---: |
| 普通 $O_B$ | $4.104980\times10^{-8}$ |
| 普通 $O_C$，含物理 even mean | $3.710780\times10^{-8}$ |
| divergence 模块 $D_B$ | $1.674413\times10^{-7}$ |
| divergence 模块 $D_C$，含完整诱导高模 | $1.428850\times10^{-7}$ |

采用原四个完整物理 Green 增益，有
$$
\mathcal E_H(Tw_0)<1.029516023\times10^{-5}.
$$
再乘且仅乘一次原 Hessian resolvent，得到新的特定方向加性费用
$$
a_H(w_0)<1.033484771\times10^{-5}. \tag{A.1}
$$
原全部 97 列 HS 上界再乘 $\|w_0\|$ 给出的对应预算小于
$1.372740655\times10^{-5}$。因此 (A.1) 是有效但有限的收紧。两项 divergence 费用仍是主要预算组成；这些数值均是上界，不是实际误差的下界，也没有证明响应门已闭合。

## 2. 完整性及没有重复的原计算

原 local native 为
`bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd`，
原 97 列 Hessian native 为
`cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26`。
新算术完整读取二者；原物理帽 residual cells、target、primitive、endpoint 和 mean 流没有重算。

每个真实交格先右乘 $w_0$，普通源按准确 Legendre 恒等式积分。divergence 先逐 Fourier 槽取 Bernstein 径向上确界，再跨格及跨模式求和，没有额外径向长度因子。物理非均值槽的 Gram 因子是 $1/2$，even mean 的因子是 1。

准确 $9/10$ 与首个 binary64 数组节点被分别保留。原 cf055 producer 和本消费者都包含二者之间同一首三次多项式的极短延拓，因而首行的新方向界与原 HS 界均覆盖整个真区间。每行只在同一标量源范数的两个合法上界之间取较小者，没有替换多项式余项。

## 3. 准确使用合同

若已成完整物理源给出 $\varepsilon_{\rm phys}(w_0)$，则本次新结果授权
$$
\varepsilon_{\rm mov}(w_0)
 \le 1.003854965\,\varepsilon_{\rm phys}(w_0)
       +1.033484771\times10^{-5}. \tag{A.2}
$$
每个系数均已向外取整。若要作用于连续 $Z$ 的准确 cut even 输入 $e_Z$，仍须加
$$
\|\mathcal E_{\rm old}\|\,\|e_Z-w_0\|.
$$
这里使用原完整 moving **误差算子**范数。单个方向的改进没有转授给未知输入。true97、独立 mean 和 known high 输出继续保留其原 cut 变换与全部费用。

## 4. 原件身份和真实 pull

验收目录为
`notes/particular_cap_Hessian_ci/run-43616252389-1-same-w0-particular-cap-Hessian/`。

| 文件 | SHA256 |
| --- | --- |
| native/complete-same-w0-particular-cap-Hessian.json.gz | 9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650 |
| process.json（本次仓库快照） | d3af78ba64ff5f4f6dca4a5bb66bda6f3158ea12cb7eeda69e0e0331099c69d5 |
| evidence/complete-same-w0-particular-cap-Hessian-summary.json | 25a788b030b7082f98b1a1f29dfca40f4e0a838627b30f7965695614a926fe14 |
| 科学 source | f5d1f3ffc96f631076d22768d0e4999ba7357231d9f63d8ec68113a3fc7d1cff |
| worker | 9d4e781665ee61de9f99caea51070f87b5d1c62c7106ae4190f0af6a683b7531 |
| 输入 manifest | 47d24bca452b483a9320d89ff707cc273f4a3bff77a0c2bb4b71d5d89d48168d |

完整 native 为 1550110 字节，小摘要为 11597 字节。artifact 名为
`visible-exact-particular-cap-Hessian-43616252389-1`。仓库与 artifact 的 process 出版快照分别按真实字节核验，不假定 SHA 相同。该过程执行了真实 pull 与两份 README 差异检查；最后读取提交
`5fd683323dea40a4400fdb3437a990838762bd17`，差异为空。

数学说明见[特定方向 Hessian 合同](../notes/2026-11-14-R133-particular-cap-Hessian-contract.md)。本次只付清 (A.1) 的特定源；完整 cut、同 $Z$ 有限 Green 合成、未知 high 反馈以及完整 PDE 响应与非线性存在论仍由各自证书继续处理。
