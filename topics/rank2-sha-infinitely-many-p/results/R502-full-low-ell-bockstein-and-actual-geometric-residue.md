# R502 — 低 ell 全首 Bockstein、活着的 V1 项与真行剩余配对

日期：2026-11-14。**状态：已证明。** 在 R498 的同一实际低 \(\ell\) 立方窗，本篇给整个相对首 Bockstein 的正规坐标闭式，保留全部 Gaussian、原 \(t/w\) carry 单位及来源的第一法向单位项 \(V_1\)。该项在 \(r>2k\) 时确能落入原第二块，不能先按 \(3C\) 截断删除。

再将全强迫经原低行消元配到 R498 的真左行，得到一个包含真实 \(\xi\)、两项 carry 和实际低行修正的完整剩余式。没有由任何单独单位项宣称非零；原 \(M\) 的十三行边界及第三精度仍按既有公式保留。

恢复记录：完整正文在执行环境断连前已由主代理读完，现据该全文恢复保存。原有限证书脚本未及推送；现已按同一个实际来源重建，并于公开 Actions 实际复现全部 81 行。第9节保留重建身份、来源提交和原始日志，正文证明不依赖扫描。

## 1. 实际范围和同一因子化基准

保 R491、R495、R498 的原单 \(Y=\mathscr R\) 来源。选择 R491 已付的真正因子化整基准
\[
P^{\rm fact}=d^{-C_D}t^r\widetilde F^{\,3}\widetilde Q\in\mathcal W_D,
\qquad \bar P^{\rm fact}\in\ker\bar J.
\]
以下省略因子上的波浪，始终使用这个同一提升。令
\[
h=\operatorname{ord}_w\bar F(t(w),\bar g(w)),\qquad
k=2h+r-s.
\]
本篇的低 \(\ell\) 范围为
\[
\boxed{1\le\ell\le r<h,\qquad 0\le k<\ell,\qquad p=6s-1>83.}
\tag{1}
\]
于是 \(s=2h+r-k<3h\)，\(h+k<s\)，原两条 carry 均可读。
不额外要求 \(r>2k\)；只有提取某条更低值行时才使用这一条件。

令 \(\widetilde\psi(t)\in\mathcal O[[t]]\) 为所选 \(F\) 的原 Hensel 单位分支。
其常数可在 \(1+p\mathcal O\) 中，不强行设为 \(1\)。定义
\[
\zeta=\log(Y/\widetilde\psi(t)),\qquad
\eta=\log(g/\widetilde\psi(t)).
\tag{2}
\]
这里都在原有限 \(\Gamma/p^2\) 中使用下文的有界 log，不调用原窗口之外的整性。写
\[
\boxed{\eta=t^h u(t)+p\xi(t),\qquad
\xi\in\mathcal O[t]_{<h},\quad u(0)\in\mathcal O^\times.}
\tag{3}
\]
这个 \(u\) 是 **log normal 坐标的系数**，不是 R459 的 \(F(t,g)\) 接触单位；
两者的首项相差 \(e_0=(\mathcal EF)(0,1)\) 及 \(t/w\) 的已知首单位。

## 2. 原有限目标中的 log 真的只用到五次

原关系仍是
\[
\Gamma=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2).
\]
在 \(\Gamma/p^2\) 中，理想 \((p,w^h,\epsilon)\) 的六次幂为零。逐项证明如下：

- 含两个 \(p\) 或三个 \(\epsilon\) 的项为零；
- 不含 \(p,\epsilon\) 的六次项含 \(w^{6h}\)，而 \(6h>2s\)；
- 含一个 \(\epsilon\) 的项在 \(w^{s+\ell}\epsilon\) 后为零，且 \(s+\ell<4h\)；
- 含两个 \(\epsilon\) 的项在 \(w^\ell\epsilon^2\) 后为零；
- 含一个 \(p\) 的其余项由 \(pw^s=p^2\epsilon=0\) 及同一第三块截断消掉。

所以 \(\log(1+x)\) 和 \(\exp(x)\) 只需至五次，所有分母在 \(p>83\) 为单位。
因为 \(Y/\widetilde\psi-1\) 属于这个理想，(2) 确实为整的有限坐标，并准确有
\[
\boxed{\zeta_{\rm phys}=\eta+a\epsilon,\qquad a=p\kappa\in\mathcal O^\times.}
\tag{4}
\]
这里保原 Gaussian 单位 \(a\)；不是把 full log 的 \(p\) 分母略掉。

原参数逆 \(w=w(t)\) 为整单位变换，置
\[
b_s(t)=\left(\frac{t}{w(t)}\right)^s\in\mathcal O[[t]]^\times.
\]
同一个目标中准确有
\[
\boxed{t^s=p\epsilon\,b_s(t).}
\tag{5}
\]
后文始终使用整个 \(b_s\)，不只其首项。

## 3. 全单位与完整正规二次强迫

将实际来源写为
\[
P^{\rm fact}=t^rV(t,\zeta)\zeta^3,
\qquad
\boxed{V(t,\zeta)=d^{-C_D}Q(t,\widetilde\psi e^\zeta)
\left(\frac{F(t,\widetilde\psi e^\zeta)}{\zeta}\right)^3.}
\tag{6}
\]
它是原窗口中的整单位。模 \(p\) 后记
\[
\eta_0=t^hu,\qquad V=V_0+V_1\zeta+\cdots,\qquad
e=(\mathcal EF)|_C,\quad f_2=(\mathcal E^2F)|_C,\quad
q=(d^{-C_D}Q)|_C.
\]
准确有
\[
\boxed{V_0=qe^3,\qquad
V_1=d^{-C_D}\left((\mathcal EQ)e^3+\frac32Qe^2f_2\right)\Big|_C.}
\tag{7}
\]
\(Q,e,f_2\) 均来自同一个实际因子及基准。

定义同一首 Bockstein 代表
\(\beta_J(P^{\rm fact})=\overline{J(P^{\rm fact})/p}\in\bar\Gamma\)。
这里 \(J(P^{\rm fact})\) 已被 \(p\) 整除，但未假定被 \(p^2\) 整除。

**定理1。** 在原整个有限目标中，
\[
\boxed{\beta_J(P^{\rm fact})
=\operatorname{ev}_{\zeta=\eta_0+a\epsilon}
\left[V\left\{
3t^r\xi\zeta^2+
\frac{b_s}{a}t^ku^2(3\zeta^2-5\eta_0\zeta+2\eta_0^2)
\right\}\right].}
\tag{8}
\]
所有系数在本式取模 \(p\)，全部来源与单位仍为 (3)、(5)–(7)。

**证明。** 先在 \(\Gamma/p^2\) 展开
\[
t^r(\eta+a\epsilon)^3
=t^r(\eta_0+a\epsilon)^3+
3pt^r\xi(\eta_0+a\epsilon)^2.
\]
\(t^r\eta_0\epsilon^2=0\)，因为 \(r+h\ge\ell\)。
由 \(r+2h=s+k\)，两个真正 carry 为
\[
t^r\eta_0^3=p\epsilon b_st^{h+k}u^3,\qquad
3at^r\eta_0^2\epsilon=3ap\epsilon^2b_st^ku^2.
\]
余下的 \(p\xi\) 普通项含 \(pt^{s+k}=0\bmod p^2\)；
其第三块项因 \(r\ge\ell\) 为零，第二块完整保留。
除 \(p\) 后，将 \(\epsilon=(\zeta-\eta_0)/a\) 代回：
\[
\eta_0(\zeta-\eta_0)+3(\zeta-\eta_0)^2
=3\zeta^2-5\eta_0\zeta+2\eta_0^2.
\]
同时 \(3t^r\xi\zeta^2\) 的其他两项在原约化目标为零。
最后乘整个 \(V\)；原三次括号已被 \(p\) 整除，所以其 \(p\) 次单位修正不再影响除 \(p\) 后的约化。证毕。

## 4. V1 为何真的活着

在原 \(\bar\Gamma\)、(1) 的范围，准确有
\[
\boxed{\zeta^4=0,\qquad \zeta^3=3a\eta_0^2\epsilon.}
\tag{9}
\]
后一项在 \(2h<s\) 时一般非零。不能因为源高块可在 \(3C\) 上比较，就先在整个原目标令 \(\zeta^3=0\)。

乘入 (8) 可进一步准确化为
\[
\boxed{\begin{aligned}
\beta_J(P^{\rm fact})={}&
\epsilon V_0\left(b_st^{h+k}u^3+6at^{r+h}u\xi\right)
+3a\epsilon^2V_0b_st^ku^2\\
&+\epsilon V_1b_st^{2h+k}u^4.
\end{aligned}}
\tag{10}
\]
证明中的关键恒等式是
\[
\zeta(3\zeta^2-5\eta_0\zeta+2\eta_0^2)
=a\eta_0^2\epsilon
\quad\text{于 }\bar\Gamma,
\]
而再乘一个 \(\zeta\) 即零。\(V_{\ge2}\) 全消，\(\xi\) 项也只读 \(V_0\)。

最后一项可读当且仅当
\[
2h+k<s\quad\Longleftrightarrow\quad r>2k.
\tag{11}
\]
所以它正落在 R459 单位 \(-2\) 的同一低值可读范围内；删去它会改变完整首 Bockstein。
(10) 的第一块为零，第二块的最初 \(r\) 行也为零；第三块的整个实际强迫为
\[
T_2(t)=3a\,b_st^ku^2V_0\bmod t^\ell.
\tag{12}
\]
它不含 \(\xi\)。

## 5. 接整个原真行前，先保实际低行修正

使用 R498 第4节固定的原低行右逆，令
\[
L_\beta=\mathscr L_{\rm low}(0,0,T_2)
\in\overline{\mathcal W}_D.
\tag{13}
\]
此处的零同时指定第一、第二块最初 \(r\) 行。
所以 \(\beta_J(P^{\rm fact})-\bar J L_\beta\) 的所有低行都零，第三块整段零。
\(L_\beta\) 是由真实列求出的唯一所选右逆值，不是自由边界函数。

令 \(S=s-r\)、\(q_{\rm phys}=d^{-C_D}Q(t,Y_{\rm phys})\)。
在剩余高双块中，完整规范化为 \(t^{-r}q_{\rm phys}^{-1}\)；
这是取已知像后进行的目标操作，不在来源中除 \(t^r\)。
记 \(\bar J L_\beta\) 的前两块经同一规范化为
\[
\ell_0(t)+\epsilon\ell_1(t)
\in k[[t]][\epsilon]/(t^S,\epsilon^2).
\tag{14}
\]
必须保其全部高尾。

对于 (10) 的前两块本身，规范化结果第一分量为零，第二分量准确为
\[
\boxed{
G_1=b_se^3u^3t^{h+k-r}
+6ae^3u\xi t^h
+\frac32b_se^2f_2u^4t^{2h+k-r}\pmod{t^S}.
}
\tag{15}
\]
(7) 中的 \((\mathcal EQ)e^3\) 并非凭空删除：
\(q_{\rm phys}^{-1}\) 在 \(Y=g=\psi e^{\eta_0}\) 的真实一次展开，恰取消该项。
二次展开贡献从 \(t^{3h+k-r}\) 起，高于 \(S\)，因为 \(r<h\)。
\(\xi\) 项的一次单位修正从 \(t^{2h}\) 起，也高于等于 \(S\)。
因此 (15) 保住实际 \(f_2\) 项及正确成本。

## 6. 完整首 Bockstein 与原真左行的剩余式

取 R498(13) 的真正原左行 \(\Phi\)，写
\[
\Phi=(A+B\zeta+C\zeta^2)\frac{dt\wedge d\zeta}{\zeta^3},
\qquad A-2\eta_0B\text{ 正则},\qquad
A,B,C\in t^{-S}k[[t]].
\]
仍保该文的全局 \(K_X|_{3C}\) 条件和其余全部原列测试。

对于高双块 \(z_0+\epsilon z_1\)，使用
\(\epsilon=(\zeta-\eta_0)/a\) 得其准确作用
\[
\operatorname{Res}_{P}
\left(Cz_0+\frac{B-\eta_0C}{a}z_1\right)dt.
\tag{16}
\]
定义实际低行贡献
\[
\Lambda_{\rm low}(\Phi)=
\operatorname{Res}_{P}
\left(C\ell_0+\frac{B-\eta_0C}{a}\ell_1\right)dt.
\tag{17}
\]

**定理2。** 对同一个原首 Bockstein 和同一个真左行，
\[
\boxed{\begin{aligned}
\langle\Phi,\beta_J(P^{\rm fact})\rangle
={}&\operatorname{Res}_{P}\Bigg[
\frac{b_s}{a}e^3u^3t^{h+k-r}B
+3e^3\xi A\\
&\qquad+
\frac{b_s}{a}u^4t^{2h+k-r}
\left(\frac32e^2f_2B-e^3C\right)
\Bigg]dt-\Lambda_{\rm low}(\Phi).
\end{aligned}}
\tag{18}
\]

**证明。** 将 \(z_0=-\ell_0\)、\(z_1=G_1-\ell_1\) 代入 (16)。
\(C\) 乘 \(\xi\) 项的额外 \(\eta_0\) 后从 \(t^{2h}\) 起，
\(C\) 乘 \(f_2\) 项的额外 \(\eta_0\) 后从 \(t^{3h+k-r}\) 起；
二者均不产生剩余。
余下 \(\xi\) 项为 \(6e^3\xi\eta_0B\)，由 \(A-2\eta_0B\) 正则，
乘正则的 \(3e^3\xi\) 后剩余相同于 \(3e^3\xi A\)。
其余两项正是 (18)。证毕。

因此这个固定首核能相对提升到模 \(p^2\)，当且仅当 (18)
对整个原真左行空间全为零。这是原有限自由线性映射的准确首次可解性判据，不要求先保持因子。
改变低行右逆只改变中间表示；真行杀所有原像，所以最终值不变。

式 (18) 的四个部分都属于同一真实问题：
原第一 carry、实际 \(\xi\) 的极配对、活着的法向/第二 carry 混合项、
以及原低行高尾。不能只取其中一个单位项判非零。

## 7. 同一提升选择与未付的真实输入

R491 允许选取因子化实际基准，但不允许任意指定 \(\xi\)。
若改用另一组仍保持原来源的因子提升，两个基准相差 \(p\) 倍原来源，
故 (18) 在真左行上的值不变。这只消去可由实际因子变形产生的
\(\xi\) 变化，不意味着任意低次形式 \(\xi\) 都可被消去。

R498 的 ODE 转置准确止于首共振之前；
(18) 现明确显示其下一精度所需的真实量是
\(3\operatorname{Res}(e^3\xi A)\)，以及原低行和活着的 \(f_2\) 项。
这些仍须使用同一实际 Miller forcing、完整中央及原左行提升来控制。
没有把 \(\xi=0\) 当作合法规范选择。

## 8. 原 M、十三行边界及第三位

本篇得到的是整个相对 \(J\) 的首 Bockstein，而非原 \(M\) 的完整提升判据。
原矩阵始终为
\[
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
\]
所以若只求原 \(M\) 的模 \(p^2\) 提升，仍须允许 R479 的同一 \(B_0,B_1\)
carry 输出并经 \(\pi\) 投影；不能将 (18) 对全部相对左行全零误称为原 \(M\) 必要条件。
进入下一位则严格用 R481 的同一首次修正、完整第二障碍和到 \(G_2\) 的投影。

\(P_{134}/U_0\)、十三自由行、两条十三行 carry 和完整 Gaussian 均未缩短。
本篇没有证明 (18) 的跨 \(p\) 非零，也没有增加任何乘积来源的中央零。

## 9. 同一个真实低 ell 立方的固定证书记录

断连前脚本 check-r502-full-low-ell-bockstein.py 只使用此前 R475 的一个实际来源：
\[
p=239,\quad D=40,\quad \ell=1,\quad
(r,h,k)=(10,15,0),\qquad
H_DY^{37}(Y-\rho_{<15}(t))^3.
\]
原执行逐列保 charge \(37,\ldots,40\) 的多项式帽，
直接评价完整 \(81\) 行的 \(J(P)/p\)，与 (10) 全部相同。
本例实际 \(\xi\) 非零；\(\zeta^6=0\bmod p^2\)，
但 \(\zeta^3\ne0\bmod p\)、\(\zeta^4=0\bmod p\)。
被保留的 \(V_1\) 项在从零编号的原相对第 \(70\) 行首现，系数为 \(55\)。
完整 \(Q\) 单位运输后的式 (15) 也逐行相同。

原脚本在断连前未推送，现已重建同一固定来源。公开 Actions 的
[运行 43596695716](https://github.com/Rogerhu12/math-research-public/actions/runs/43596695716)
于 2026-11-14 12:49:37 UTC 实际执行成功；job 为 132452617972。
实际 checkout 来源提交为
`1dafbfa774b9232c561b48def4d8a61d2117837c`，工作流先核对完整提交号再执行脚本。

保存的 [重建脚本](../scripts/check-r502-full-low-ell-bockstein.py)、
[原生 JSON](../scripts/check-r502-full-low-ell-bockstein.json) 与
[完整运行日志](../notes/2026-11-14-r502-recovered-actions.log)
准确记录：81 条相对行全部一致，实际 ξ 的一次系数为 175，
活 V1 首行 70、系数 55，第三块常数 40，
原 ζ³ 非零、ζ⁴ 为零及模 p² 的 ζ⁶ 为零，完整物理 Q 单位运输全部通过。
JSON 明示 `certificate_identity=reconstructed_after_workspace_disconnect`、
`prime_scan=false` 与 `central_zero_or_nonzero_claim=false`。
该次执行是明确标识的重建证书，不冒称丢失脚本的原字节；
这个单一有限例也不构成跨 p 非零结论。
