# R133 supplement: actual finite part at the selected explicit-family parameter

2026-11-14, visible-exact-astra-0df9.

**已证明（同一显式族、原 $\eta_0$）：**
公开 [43597209022](https://github.com/Rogerhu12/math-research-public/actions/runs/43597209022)
实际完成全部十二项检查，数学子进程和发布 worker 均退出 0。
原 169 scalar germs、626 scalar cells、220 compact-$T$ 模型、
3146 已完成积分区间、两个 root Newton 步以及 R31 证书全部复用。
新计算只支付完整有限部的参数导数，不重新生成任何这些原对象。

记 $\delta_*$ 为已实际证明的 R31 显式参数，且
$|\delta_*|<9.368259853002\,10^{-11}$。
在同一 $Q_\delta=\bar Q+\delta Z,\ \nu_\delta=\nu_0+\delta,\ \eta_0$ 中，
完整首符号有限部满足
$$
\boxed{
 -73.913354970078433
 <\mathfrak X(\delta_*)
 <-73.913297220108052 .
}
$$
对应的有向标量倍数为
$$
\boxed{
 18.478324305027005
 <-\mathfrak X(\delta_*)/4
 <18.478338742519616 .
}
$$
此倍数不是尚未完成的完整返回系数 $\beta$。

## 1. 原件与实际执行

数学源为
[first_symbol_parameter_transfer.py](../scripts/fourfold_codazzi_first_symbol_parameter_transfer.py)，
SHA256
`de12b8129caeb8c51857f6b44a152c7a91e1facbdc553d2bd4f4ea320a38406a`。
固定 179 文件 manifest 为
`fb578b1d081920a8a75fe58fea0468f5ea58e629f74e4479f9b69f1c63cb2cc5`，
独立 CI driver 为
`6cfaf94a8ca66bead4b442b7ecf280260656072b1d13f1e72ed053af773289b9`。
该 manifest 引用已经发布的条件定理正文，未恢复旧未发布版本。

原 [数学过程](../notes/first_symbol_parameter_transfer_ci/run-43597209022-1/consumers/process.json)
SHA256 为
`78cbf8e6b207f23f2d2302ac76c09ca5de58a2a308e40e71aff28dc64eec0d47`；
它包含十二项真实门及这里引用的完整有向输出。
原 [native](../notes/first_symbol_parameter_transfer_ci/run-43597209022-1/consumers/first-symbol-parameter-transfer.json.gz)
为 1,403,016 bytes，SHA256
`06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb`。
native 保全部逐格预算及四个根 Cauchy 半径的输出。

事件提交是 cbd5c90ba2549d833423faef7f6c9fdfd1e51b7a；
实际 immutable 科学副本来自
5e14fd1de48f7c51dbe465cebef048c3d948fc76。
二者分别记录。数学子进程墙时 10.037203505 秒，
外 worker 墙时 10.336783346 秒；真实运行环境为 Python 3.12.14、
python-flint 0.9.0、256-bit Arb。

## 2. 完整参数同伦的预算

使用[完整参数转移定理](R133-supplement-first-symbol-finite-part-parameter-transfer-contract.md)
(D.9)、(D.17)、(D.18)。实际向外取整可取
$$
 L_{\rm strict}<46290.115024193,\qquad
 L_{\rm root}<140461.873596045,\qquad
 L_{\rm total}<186751.988620238 .
$$
其中 strict 预算消费全部 3146 个原区间，没有只使用若干测试格。
每个区间重新限制已经证明的完整七阶 Taylor 恒等式，
原点 jet 是除以阶乘的 Taylor 系数，导数限制还保全区间七阶余量。
compact-$T$ 的全部 220 个原模型均进入消费。

根处 compact bump 准确为零，故根、$K,b,\gamma$ 不随 $\delta$ 移动。
复根完整 193 方向、独立 even mean、$\eta^{-1}$ 和 $k$ 的正间隙
来自已经成功的完整 root 预算。$k_\rho$ 由原复域 $k-60$
包络与实际 Cauchy 半径支付，不从实轴一阶导数捏造二阶导数。
两个非可积首项在积分之前准确扣除，$D$ 系数的第二项没有额外
$\eta^{-1}$。

因此整个选定参数同伦满足
$$
 |\mathfrak X(\delta_*)-\mathfrak X(0)|
 \le |\delta_*|L_{\rm total}
 <1.749541157460\,10^{-5}<10^{-4}.
$$
把这一费用以对称有向区间加到实际完整
[v2 $\delta=0$ 有限部](R133-supplement-actual-complete-moving-first-symbol-finite-part.md)
上，即得开头两个区间。这是同一显式族的转移，
没有更换回未修补中心或假设真正 PDE 分支已经存在。

## 3. 与实际返回算子的接口

[有向 word](R133-supplement-directed-return-word-and-root-first-coefficient-contract.md)
已固定 $P=S_-\circ X_+$、density 规范和物理频率 $4j$。
这里支付的部分为 $-\mathfrak X(\delta_*)/(4j)$。
完整 root/positive 图仍须给同一规范中的
$-b_{\rm root}^{\rm fin}/(4j)$ 及所有保留接口，
并支付所需 Sobolev 窗的强余项。还必须把显式族与真正 PDE
背景连接。十二项门与上面区间均不把这些剩余量设为零。
