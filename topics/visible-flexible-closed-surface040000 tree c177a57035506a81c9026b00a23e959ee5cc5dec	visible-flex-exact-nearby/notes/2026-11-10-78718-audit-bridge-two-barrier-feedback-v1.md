# 同一精确桥的双屏障反馈：全文独立审查

日期：2026-11-10。审者：Astra-visible-flex-78718bd0 / independent_audit。

## 0. 结论、条件量词和审查身份

**全文数学与实际有限证书独立重跑通过。** 正式稿请补明相位门的参数和频率范围：$\gamma>0$、有限 $q\ge0$；若该门只在 $|n|\ge N$ 检查，则 (26) 先只在该高频范围成立，全空间常数还须并入有限低模的真实最小值。这是把原条件陈述的量词写全，不表示当前相位门已验证。

原稿 [geometry-bridge-two-barrier-feedback-v1](2026-11-10-78718-geometry-bridge-two-barrier-feedback-v1.md)，9860 B，SHA256 `9336712dd04a7fc8ecd29b72997a3284074a11b4f4b65bea2da8ef3de075fbaa`，全文六节已实际读取（`ae6974`、`2b7607`）。本审未参与其构造、未参与主候选或参数优化。原稿保持冻结。

通过的是 R21 同一精确径向背景的桥相位／势结构、正势外区双向传递界，以及两个准确模块的普通源反馈公式。没有重新选择桥、度量或 cut，没有给本轮新有限图移用旧 metric-transfer 证书，也没有证明实际高频相位门、原端口反馈逆或闭曲面。

## 1. 已审精确桥依赖与实际来源

接受 [R21 §2](../results/R21-m12-whole-map-and-actual-metric-decrease.md) 已审的同一唯一 exact bridge。本审此前已实际读该节；本次又读取旧 exact-bridge 程序 `main` 的实际常数／根盒／目标转移接口（`eedfd5`），核实 `length.lo>3/5`、`length.hi<7/10` 是该原证书明确执行的严格门，$p_s=(-7w/a_c)/E^{3/2}$、$w=1/2$ 也不是本稿新选择。原 [exact-bridge 证明](2026-11-09-db6f-exact-bridge-and-metric-transfer.md) 已全文读过，旧唯一根存在性和有理包围不在本次重开。

当前有限检查真实记录的三份来源为：

| 相对本题路径 | 字节数 | SHA256 |
| --- | ---: | --- |
| `results/R21-m12-whole-map-and-actual-metric-decrease.md` | 14695 | `3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c` |
| `scripts/db6f-root-exact-bridge.py` | 9408 | `f5d10784f58fa5008220354665de710ab4991b795f1b902e26a70ca44f382fd1` |
| `repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py` | 5123 | `85b9e746235a32c3e78229d6d1ddc424ee3497db3a8d61c858b14bc6534bf468` |

这些是实际源身份，checker 没有伪称重新计算原根；原根作为已审依赖使用。原 DirectionalBridge 的 cubic turn／profile 与本稿写法同一：$d=-Lp_s>0$ 时
\[
\varphi(t)=p(3t^2-2t^3)+Lp_s(t^3-t^2)
=(3p+d)t^2-(2p+d)t^3.
\]
其终值 $\varphi(1)=p$、终弧长导数 $\varphi_s'(1)=-d/L=p_s$，与同一个物理 cut 的二阶匹配相符。

raw Target 的冻结二进桥与主精确桥的区别已经在原稿 §1 及本审前一 [actual-port 审稿](2026-11-10-78718-audit-actual-port-transfer-v1.md) 说清。背景相同不代表任何本轮新图已经完成自己的目标转移。

## 2. 相位、余弦和半径的严格全区间界

$a_c$ 是 binary64 `.6` 的精确值，确在 $(599/1000,601/1000)$。$p=\pi/2-\arctan(1/2)$ 的下界由 $\pi>3$、$\arctan(1/2)<1/2$ 得 $p>1$。四项交错 atan 部分和以负项结束，是下界；结合 $\pi/2<11/7$，精确有理比较得 $p<111/100$。

$\sqrt{5/4}>11/10$（平方比较）给 $E^{3/2}>11/8$，所以
\[
0<-p_s<\frac{7/2}{(599/1000)(11/8)}=rac{28000}{6589}<17/4.
\]
再用 $L<7/10$，得 $0<d<19600/6589<3$。这些上界同时有效，不把有关参数当相互独立的精确取值；用更大矩形盒只使后续上界更保守。

对 $0<t\le1$，$\varphi(t)=t^2[(3p+d)-(2p+d)t]\ge pt^2>0$。导数为
\[
\varphi_t'=t[(6p+2d)-(6p+3d)t],
\]
故唯一内零点是
\[
t_*=(6p+2d)/(6p+3d),\qquad 2/3<t_*<1.
\]
相位先增后减，直接代入得到最大值
$4(3p+d)^3/[27(2p+d)^2]$。该值的两个对数偏导分别有正分子 $6p+5d$ 和 $d$，所以对正 $p,d$ 严格递增。由 $p<111/100,d<3$ 给
\[
\varphi_{\max}<\frac{4(633/100)^3}{27(261/50)^2}<7/5.
\]

因 $7/5<\pi/2$，cos 在所需范围递减。其四项交错 Taylor 下界
\[
1-(7/5)^2/2+(7/5)^4/24-(7/5)^6/720>1/6
\]
确为下界：余下首项为正，后续项绝对值递减。于是完整桥上 $\cos\varphi>1/6$。这支付 $z_s>0$，不依赖原采样角检查。

由 $a_s=-\sin\varphi<0$（内部）和唯一根匹配 $a(L)=a_c$，有 $a_c\le a\le1$，故 $a>59/100$。这既给半径正性，也给后续所有坐标变换的分母下界。

## 3. 真势符号及接口正则性

由 $c=-\sin\varphi$、$\bar p=1/\cos\varphi$、$a_{ss}=-\cos\varphi\,\varphi_s'$，精确 Sturm 势为
\[
V=\frac{a^3a_{ss}}{(1-c^2)^2}
=-\frac{a^3\varphi_s'}{\cos^3\varphi}.
\]
所有前因子严格正，故在 $0<t<t_*$ 上严格负，在 $t=t_*$ 为零，在 $t_*<t\le1$ 严格正。$\varphi_{ss}''(t_*)=-(6p+2d)/L^2\ne0$，所以桥内部该零点确为简单零点。

桥起点的展开也独立核过：
\[
\varphi(s/L)=(3p+d)s^2/L^2+O(s^3),\quad
\varphi_s'=2(3p+d)s/L^2+O(s^2).
\]
而 $a=1+O(s^3)$、$\cos\varphi=1+O(s^4)$，所以
\[
V(s)=-2(3p+d)s/L^2+O(s^2).
\]
第一周期从左的末 ramp 势则按已审原 flat law 二次趋零；它与新桥的一侧线性起点不能被改写成同一个光滑简单根模型。连接处 $a,a',a''$ 相容，因此 $a\in C^2$；$V$ 连续、分段光滑、在该有限连接上绝对连续。没有声称 $a\in C^3$，也不需要这样的新增门。

第一周期已有中央负势段，随后经过第二平段和末正势 ramp，再进入桥负势段。因此全前缀是两个负势屏障之间隔着非负／正势区域，不能把单中央负势区的 Green 证明不加说明地作用于整个级联。这是符号结构结论，不是已证某个整数模共振。

## 4. 桥长度、势的完整有效界

$dr/ds=\cos\varphi/a^2$，因此
\[
R_b<\frac{7/10}{(59/100)^2}<21/10.
\]
在负势部分，$a\le1$、$\cos\varphi>1/6$、$L>3/5$、$t_*>2/3$，故其 Sturm 长度
\[
\ell_b>\frac16\frac35\frac23=1/15.
\]

记 $A_1=6p+2d<1266/100$、$B_1=6p+3d>A_1$。$\varphi_s'=t(A_1-B_1t)/L$ 的正最大值为 $A_1^2/(4B_1L)<A_1/(4L)<53/10$。在负值部分该二次式严格递减，终值为 $p_s$，故负部绝对值小于 $17/4$。综合得
\[
|\varphi_s'|<53/10,\qquad |V|<216(53/10)<1200.
\]
没有用有限网格代替全区间极值。

右正势外区取 $\omega=a^3/\cos^3\varphi$、$v_b=-\varphi_s'$。$a$、$\varphi$ 都递减，因而 $\cos\varphi$ 递增，$\omega$ 递减；又 $\varphi_{ss}''<0$，所以 $v_b$ 递增。于是
\[
1/5<\omega<216,\quad 0\le v_b<17/4,\quad 0\le V=\omega v_b<918.
\]
$1/5$ 下界由 $a_c^3>(59/100)^3>1/5$，并用 $\cos\varphi\le1$。这两个相反单调因子的处理是下节变差界的实质，不能未经证明假定 $V$ 自身单调。

## 5. 独立展开 3100 的双向正变差估计

令 $k=\langle n\rangle\ge1,m=1/k,q=\sqrt{V+m^2}$、$S=\operatorname{diag}(1,q)$，取 $W=SZ$。变换后系数为
\[
- in\begin{pmatrix}0&V/q\\q&0\end{pmatrix}
+\operatorname{diag}(0,q'/q).
\]
第一矩阵的 Hermitian 部分的 norm 是
$|n||q-V/q|/2=|n|m^2/(2q)\le|n|m/2$。第二项的正增长至多 $(\log q)'_+$，因此对真实传递可以积分该能量不等式；在反向参数上同一推导仍成立，正变差应按该方向计算。

向前时 $\omega'\le0$、$v_b'\ge0$，所以
\[
(\log q)'_+\le\frac{\omega v_b'}{2(\omega v_b+m^2)}
\le\frac{v_b'}{2(v_b+m^2/216)}.
\]
任意子区间积分得到
\[
\exp\operatorname{Var}_+(\log q)
\le\sqrt{1+216(17/4)k^2}
=\sqrt{1+918k^2}<31k.
\]
这里用起点 $v_b\ge0$，不要求子区间从零点开始。

向后时 $v_b$ 不增、$\omega$ 不减，正增长至多 $\tfrac12d\log\omega$，故指数至多 $\sqrt{\omega_{\max}/\omega_{\min}}<\sqrt{1080}<33$。两方向统一可用 $33k$。

端点变换满足 $\|S\|<31$（$V+m^2<919<31^2$）与 $\|S^{-1}\|\le k$。而 $|n|m\le1$、$R_b<21/10$，故剩余能量增长小于 $e^{21/20}<3$。因此
\[
\|T_n^{Z,b}(r_2,r_1)\|
<31\cdot33\cdot3\,k^2=3069k^2<3100k^2.
\]
这对右正势外区的任意两点、任一方向、所有整数 $n$ 成立，包含 $n=0$ 和零点端。普通源 (20) 随即由真实变常数式和正长度积分获得，没有改源或引入源导数。

此处只支付正势外区。原稿明确没有以这些输入冒称桥的完整内部普通源界已在本篇证明，也没有错误合并两个屏障。

## 6. 两模块精确接线与非齐次源

第一周期与桥在公共截面均有 $a=1,c=0,\bar p=1$，所以 $Z$ 变量及 Hadamard 通量基完全一致。无需一个被省去的接缝缩放。

每个固定 $n$ 的桥势连续、长度有限，真实 ODE 基本解存在并保持 $J$ 且行列式为一。因此同 R75 的有限维论证给桥散射的酉性及非零 transmission。这是每模实际存在，不需先有全频统一有界逆；对每个普通 $L^2$ 源，其固定模仿射输出也由变常数积分真实定义。

设 $u$ 为周期右 incoming（桥左 outgoing），$v$ 为桥左 incoming（周期右 outgoing），保持原来的 incoming/outgoing 排列。接口是
\[
v=t_c I_L+r_cu+f_R^c,\qquad
u=r_bv+t_bI_R+f_L^b,
\]
其中 $r_c=\mathcal S^c_{22}$、$r_b=\mathcal S^b_{11}$、$t_c=\mathcal S^c_{21}$、$t_b=\mathcal S^b_{12}$。消去 $v$ 精确得到
\[
\Psi_nu=r_bt_cI_L+t_bI_R+r_bf_R^c+f_L^b,
\quad \Psi_n=1-r_br_c.
\]
这核实了作者 (21)–(23) 的所有方向、矩阵角标及两个普通源列。外端的实际 support／Robin 条件是另一层反馈，不能与这里的内部消元混同。

## 7. 逐模非零、相位门及其完整频率量词

酉性给 $|r_c|^2+|t_c|^2=|r_b|^2+|t_b|^2=1$，且 transmission 对每个有限模非零。因此 $|r_b|,|r_c|<1$，$\Psi_n\ne0$。

令 $A=|t_c|^2,B=|t_b|^2\in(0,1]$。由于 $1-(A+B)/2\ge0$，并且
\[
\left(1-\frac{A+B}2\right)^2-(1-A)(1-B)=\frac{(A-B)^2}4\ge0,
\]
可合法开平方，得到
\[
|\Psi_n|\ge1-|r_br_c|\ge(|t_c|^2+|t_b|^2)/2>0.
\]
仅逐模严格正不能给全空间统一正下界，原稿在此准确保留限制。

若 $r_br_c=\rho_ne^{i\vartheta_n}$，则
\[
|1-\rho_ne^{i\vartheta_n}|^2
=(1-\rho_n)^2+4\rho_n\sin^2(\vartheta_n/2).
\]
在 $\rho_n\ge1/2$ 的模上，若**实际成立**
$|\sin(\vartheta_n/2)|\ge\gamma k^{-q}$，$\gamma>0,q\ge0$，则
$|\Psi_n|\ge\sqrt2\gamma k^{-q}$。对 $\rho_n<1/2$，有 $|\Psi_n|>1/2\ge(1/2)k^{-q}$，最后一步确需 $q\ge0$。故在已覆盖的频率集合上
\[
|\Psi_n|\ge\min(1/2,\sqrt2\gamma)k^{-q}.
\]
$\vartheta_n$ 在乘积为零时不必定义，因为它属于自动处理的第二种情况；模 $2\pi$ 的选择也不改变所需绝对正弦。

若上述门只作为高频条件在 $|n|\ge N$ 成立，要写全空间有限损失逆，还应取
\[
c_*=min\left\{\tfrac12,\sqrt2\gamma,
\min_{|n|<N} k_n^q|\Psi_n|\right\}>0.
\]
有限头部定性正性来自每模非零；有效数值常数则须有真实有限核查。本文没有该相位门或有限表，故不能在本轮宣称已有实际全空间 tame 反馈逆。

一旦声明的统一界已真正支付，$\Psi^{-1}$ 的对角乘子从 $X_w^{\nu+q}$ 到 $X_w^\nu$ 有界。每个散射 entry 的模至多 1，故接口中的 incoming 和两个 source 输出列按 (23) 以相同权运输，再损失最多这 $q$ 阶。这里须已有模块源输出的相应 norm；本稿没有借这句话跳过桥内部的源证明。其它真实外端 feedback、非径向耦合或非线性余项仍不在此结论内。

## 8. 冻结 checker 的真实独立执行

全文读取 checker `78718-geometry-bridge-two-barrier-check.py`（`c8e2ab`），SHA256 `86794b2b29ba3cbb307eb6c64488375b1d65e8aa9a791873ce7911ac93375ec6`。八个符号式分别核 turn 终值／终导、唯一临界因子和位置、最大值、起点线性势系数、AM–GM 平方差、接口普通源消元；十六条 Fraction 门核精确 binary cut、相位／余弦／长度／势／能量常数。

其中 $e^{21/20}$ 上界使用 Taylor 项到 22 阶，尾部以第 23 项为首项，后续比不超过 $(21/20)/24<1$，几何级数给严格上包围；该 Fraction 上界真实小于 3。cos／atan 的交错余项符号和全区间单调性已在本审数学部分独立核，不能只由 checker 的有限布尔值替代。

实际命令：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
scripts/78718-geometry-bridge-two-barrier-check.py
--out notes/2026-11-10-78718-audit-bridge-two-barrier-check-01.json
```

cwd 为本题目录，真实 **4e7715，自然 exit 0**。8 符号、16 有理检查全通过；0 root solve、0 PDE、0 tail、0 候选数组。独立报告 [audit-bridge-two-barrier-check-01.json](2026-11-10-78718-audit-bridge-two-barrier-check-01.json)，2084 B，SHA256 `c24bde9204804cfc303a01b141afcd9e4e287d0e8c00bfdc0a8498721a3e6325`。与作者报告相同是确定性实际重跑结果，不是复用其执行身份。

除 §0／§7 所要求的参数和频率量词澄清外，未发现实质缺口。可登记为同一精确背景的桥结构／外区传播／准确内部反馈中间模块；不能登记相位门或闭曲面完成。
