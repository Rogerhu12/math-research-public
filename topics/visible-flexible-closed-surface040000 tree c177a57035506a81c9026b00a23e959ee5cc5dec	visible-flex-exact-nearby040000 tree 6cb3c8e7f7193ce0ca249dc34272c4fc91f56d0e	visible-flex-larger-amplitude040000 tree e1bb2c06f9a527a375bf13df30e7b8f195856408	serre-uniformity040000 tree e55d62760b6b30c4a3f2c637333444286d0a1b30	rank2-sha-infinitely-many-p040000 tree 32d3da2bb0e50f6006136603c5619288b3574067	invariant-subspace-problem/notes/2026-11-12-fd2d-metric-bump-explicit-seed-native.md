# 明确 seed plateau 的同物理目标原生读取

状态：**完整字段定义与直接代数证明；实际有限检查另列。**
本件接 `fd2d_gc_raw_bump_clean.py` 的准确声明，保持旧 reader/旧报告不变。
新增 `scripts/fd2d_gc_bump_seed_native_field.py::RawBumpSeedNativeField`，
`scripts/fd2d-metric-bump-body-screen-v2.py`，以及小检查入口
`scripts/fd2d-metric-bump-seed-native-check.py`。

## 1. 不能从名称推断 lifting

新输入必须明确记录

```json
{"kind":"central_plateau","start":0.32,"end":0.55,"step":5}
```

一般公式是 $w_1(s)=1-S_5((s-s_0)/(s_1-s_0))$，两侧截断为恒 1/0。
旧权为 $w_0(s)=1-S_5(s/L_0)$，$L_0=\min(.55,.4s_{\rm end})$。
旧 physical-bump reader 明确只读取旧权；新 reader 读取保存的
`seed_weight_definition` 和 `representation_kind`，不会因为文件名含 clean
而猜它换过权重。两种 finite-field 定义分别绑定源和数组 SHA。

实际保存 mesh 原样作为 P1 定义。当前 clean producer 把
`.5799999999999992` 与 `.58` 视作概念重复的计算节点并明确重采；
reader 自己不合并它们，也不改任何实际 physical segment、$a_\delta(s)$、
角图册 $U(s,\xi)$ 或尾 lifting。删除旧计算点后的细小径向重表达差仍是
实际有限场差，不能叫字段逐位未变。

## 2. 新旧 lifting 差及全部需要的 jets

设固定 seed 曲率为 $k_*(\xi)$，$\Delta w=w_1-w_0$。
在沿用旧 reader 的全部准确表示后，新 reader 只加入
$$
\begin{array}{lll}
\Delta n=\Delta w\,k_*,&
\Delta n_s=\Delta w'\,k_*,&
\Delta n_\xi=\Delta w\,k_*',\\
\Delta n_{\xi\xi}=\Delta w\,k_*'',&
\Delta n_{s\xi}=\Delta w'\,k_*',&
\Delta m=\Delta l=0.
\end{array}
$$
所有导数均直接求 quintic 权和 seed 的解析导数，未作差分。
之后通过同一个准确图册反解和链式公式转到固定物理材料角。
这些权独立于外物理参数 $\delta$；因此 profile/tail 参数的 lifting jets
不因这个 seed 改动而增加项。Codazzi 中 $c(\delta)(l-n)$ 对 $\delta$
的导数仍要使用实际新 $n$，这由对应 provider 和完整 complement 消费器保留。

新权在 $[0,s_0]$ 恒 1，故纯中央柱上的已知准确字段
$$
l=m=0,\qquad n=k_*(u)+\text{保存的中央有限曲率增量}
$$
可以由恒定径向修正表示；不会被一个人为从 $s=0$ 开始衰减的 seed 权强迫
产生高模径向导数。这里只说明有限表示包含了这个已知精确柱，未假定整个
前缀存在所需强解。

## 3. P1 重表达为什么仍有真实字段差

给定任意固定 retained seed 函数 $k_{m low}(\xi)$，令
$k_{m high}=k_*-k_{m low}$，$I$ 表示新 mesh 的精确 P1 插值算子。
若理想的新修正定义为
$$
\nu_1=I\nu_0+I(w_0-w_1)\,k_{m low},
$$
则新旧实际 $n$ 满足准确恒等式
$$
n_1-n_0=(I\nu_0-\nu_0)
 +[I(w_0-w_1)-(w_0-w_1)]k_{m low}
 +(w_1-w_0)k_{m high}.
$$
证明仅将 $n_i=\nu_i+w_i k_*$ 代入并合并，未要求所选 retained
系数恰好等于理想实数 Fourier 积分。实际代码把新系数保存为 binary64 时，
还应把该保存值与上式理想插值的差作为额外有限 P1 项；当前报告给的是浮点
有限比较，不凭这些小差得到区间证书。

因此低模补偿不能把真实高模变化偷偷删掉。原 producer 已明确保存该变化；
本 reader 直接读其实际新修正值，不再次补偿，也不自行重新求出更小变化。

若仅改变辅助 $n$，而物理 $l,m$ 和中央曲线完全相同，则固定材料角的
真实 frame/位置 ODE 及初值完全相同，所以唯一解 $F,X$ 及其二 jets 相同。
这说明只重写 seed 不会自动改善实际位置图；必须通过后续真正求解使
Gauss/Codazzi、实际 metric 和几何一起改善。当前 clean 的 P1 重采还可能
改变 $l,m$ 的有限求值，因此未把这种条件恒等式直接当成其 actual body 已算过。

## 4. C² 与 body 语义

新 seed 权为 C²，所有实际 P1 节点值和角 jets 仍共享。
R133 和原 physical-bump note 的连续系数 frame/角变分 ODE 论证逐字适用；
无需全局 C¹-II 或 C³ 门。

body v2 的 CLI 与 v1 相同，但明确使用 `RawBumpSeedNativeField`，并把权重
声明、表示标签、实际 mesh、全部 $\delta$、base $T$、source 和 packets
一并写入定义。实际 Gram/法向/QR 曲率和一次 proper cut 两jet配准复用同一
已检查的几何 consumer。它仍只是有限诊断，当前不对未收敛场积分。

## 5. 本次实际输入检查

准确输入为 `notes/2026-11-12-fd2d-raw-bump-clean01-warm.npz`，
SHA `aa8046eec9da82f70fe89964d7553ab9691e1b2f0000719c2e6b19c1d043454f`，
99 个保存节点。本检查没有改其任何参数、节点或修正值。

**70752 / b23fcf 实际退出 0，18.856 秒。**
与同一 `CleanRawBumpDAE` 的全部节点函数对照：

| 字段 | 最大绝对差 |
|---|---:|
| 完整 $n,m,l$ | $9.881\cdot10^{-15}$ |
| 完整一阶角导 | $1.821\cdot10^{-13}$ |
| 完整实际径向一导 | $1.365\cdot10^{-12}$ |

修改后的 seed 衰减区中，固定材料角径向链式导数小探针的 scaled $L^2$ 差
为 $1.536\cdot10^{-9}$；节点两侧角 jets 共享、定义往返逐位同，24 态 RHS 有限。
源字节在检查期间未变。报告并未把这个真实初猜称为收敛解。

body v2 另实际完成绑定入口检查 **39468 / 4c43cf，退出 0**，确从同一
producer 报告匹配了该 field SHA，选择 `RawBumpSeedNativeField`，读取准确
`.32/.55/5` plateau 声明；没有运行 body 积分。

