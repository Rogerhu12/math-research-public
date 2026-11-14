# R595 — 原 S34/T72 对角、同一参数的真实 connection 与四行整单位比较

日期：2026-11-14。**状态：已证明。**

本篇把 R398/R402/R409 的两条原算术首对角，与 R586/R591 的两个指定惰性 forcing，放在同一个真实参数、同一组原系数中比较。
得到一个在全部共同好惰性素数处可逆的固定二乘二矩阵，但完整比较是**仿射式**：两份低阶整卷积必须保留。
因此原完整中央同时消失确实给两个显示方程；它尚未推出两个辅助 forcing 同时为零，更未排除原中央同时消失。

所有等式使用同一个 sigma 来源。没有另选 theta 截面，没有把实际递推系数视作自由变量，也没有把普通负矩换成这里的惰性系数。

## 1. 原四条系数与共同参数

取
\[
 p=6s-1\ge23,\qquad N=s-1\ge3,\qquad b\in\mathcal O^\times .
 \tag{1}
\]
共同物理来源可取 \(b=17\)；与 \(E_{24}\) 的变量及整体单位运输仍按 R398/R402。
在
\[
 E_b:y^2=x^3+b,\qquad x\sim z^{-2},\quad y\sim-z^{-3},
 \quad dz=dx/(2y),\quad \sigma\sim z
\]
上使用 R591 的**同一**参数
\[
 u=x^{-1/2},\qquad t=bu^6,\qquad
 C(t)=(1+t)^{-1/2}=\sum_{n\ge0}C_nt^n,
\]
\[
 H(t)=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,\qquad
 z=uH(t),\qquad dz=C(t)\,du,
\]
\[
 K(t)=\left(\frac{\sigma(z(u))}{u}\right)^6,\qquad
 Q(t)=1+\frac{tK'(t)}{K(t)} .
 \tag{2}
\]
特别
\[
 C_0=H_0=K_0=1,\qquad C_1=-\frac12,\quad
 H_1=-\frac1{14},\quad K_1=-\frac25 .
 \tag{3}
\]
R591 的单位分母递推保证，全部次数 \(\le N\) 的这些真实系数在 \(\mathcal O\) 中。
这里只取这个窗口，不把 \(K\) 的下一 Gaussian 分母 \(t^s\) 也视为整。

记四条实际约化行为
\[
 \begin{aligned}
 A_{34}&=b^{-N}[z^{p+1}]S_b, &
 A_{72}&=b^{-N}[z^{p+1}]T_b,\\
 \mathfrak c_4&=b^{-N}[z^{p-1}](x\sigma^6),&
 \mathfrak c_1&=b^{-N}[z^{p-4}](-xy\sigma^6),
 \end{aligned}
 \qquad\text{在 }k\text{ 中读取。}
 \tag{4}
\]
此处符号 \(\mathfrak c_4,\mathfrak c_1\) 是除去共同单位 \(b^N\) 后的两个 forcing 值，不是级数 \(C(t)\) 的系数符号 \(C_n\)。
\(A_{34},A_{72}\) 是原曲线的首对角；\(\mathfrak c_4,\mathfrak c_1\) 仍是辅助来源，二者不混同。

## 2. 两个原多项式及准确的留数运输

令
\[
 P_S(t)=\frac{(1+t)(1-8t)(7-4t+16t^2)}7
 =1-\frac{53}7t-\frac{12}7t^2-\frac{80}7t^3-\frac{128}7t^4,
 \tag{5}
\]
\[
 \begin{aligned}
 P_H(t)&=(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2),\\
 P_T(t)&=P_S(t)P_H(t).
 \end{aligned}
 \tag{6}
\]
这正是 R398 原 \(S_b\)、\(T_b=S_bH_{38,b}\) 的分子，而非按前几项拟合。
从该篇全多项式式逐项代入 \(x=u^{-2}\)，准确得到
\[
 \boxed{
 S_b=u^6 K^{17/3}P_S(t),\qquad
 T_b=u^6 K^{12}P_T(t).
 }
 \tag{7}
\]
\(K^{17/3}\) 在特征零由 \((\sigma/u)^{34}\) 定义；在本篇有限窗口可按常数一的二项式级数约化。所有所需二项式分母均为 \(p\) 单位。
(6) 也准确给
\[
 H_{38,b}=K^{19/3}P_H(t).
 \tag{8}
\]
这个因子仍是原完整来源；没有给它新的中央零输入。

对任意 \(F(t)\) 使 \(u^6F(t)\) 属于当前真实来源，形式留数换元给
\[
 \begin{aligned}
 [z^{p+1}]\big(u^6F(t)\big)
 &=\operatorname{res}_{u=0}
    u^{4-p} F(t) C(t)H(t)^{-p-2}\,du\\
 &=b^N[t^N]\big(F C H^{-p-2}\big).
 \end{aligned}
 \tag{9}
\]
这里 \(p-5=6N\)；Jacobian \(C\) 与 \(H^{-p-2}\) 都不能删除。
由于 \(N<p\)，在所需整截断中 Frobenius 给
\(H(t)^p\equiv1\pmod{p,t^{N+1}}\)。
于是原两行准确成为
\[
 \boxed{
 A_{34}=[t^N]K^{17/3}P_S\,\frac C{H^2},
 \qquad
 A_{72}=[t^N]K^{12}P_T\,\frac C{H^2}.
 }
 \tag{10}
\]
同样，\(x\sigma^6=u^4K\)、
\(-xy\sigma^6=uK(1+t)^{1/2}\)，完整留数分别给
\[
 [z^{p-1}]x\sigma^6=b^N[t^N]KCH^{-p},
\]
\[
 [z^{p-4}](-xy\sigma^6)=b^N[t^N]KH^{3-p}.
\]
约化后正是 R591 的
\[
 \boxed{\mathfrak c_4=[t^N]KC,\qquad \mathfrak c_1=[t^N]KH^3.}
 \tag{11}
\]
(9)–(11) 使用相同 \(u,t,K,H,C\)，所以以下四行可直接比较。

## 3. 原对角的准确 connection 行

定义有限系数泛函
\[
 \mathcal L_p(F)=[t^N]F\,\frac C{H^2}.
\]
从真实形式对数方程
\[
 H+6tH'=C
\]
得到
\[
 \frac C{H^2}=H^{-1}-6t(H^{-1})'.
\]
对系数提取作有限分部积分，再用
\(6(N+1)=p+1\equiv1\pmod p\)，有
\[
 \boxed{
 \mathcal L_p(F)=6[t^N]\frac{F+tF'}H.
 }
 \tag{12}
\]
具体说，
\([t^N]Ft(H^{-1})'
 =N[t^N]FH^{-1}-[t^N]tF'H^{-1}\)，
而 \(1-6N\equiv6\)，故没有边界项遗漏。

对原 \(F=K^aP\)，
\[
 F+tF'=K^a\big((1-a+aQ)P+tP'\big).
\]
所以 (10) 同时等于
\[
 \boxed{
 A_{34}=[t^N]\frac{K^{17/3}}H
       \big((34Q-28)P_S+6tP_S'\big),
 }
 \tag{13}
\]
\[
 \boxed{
 A_{72}=[t^N]\frac{K^{12}}H
       \big((72Q-66)P_T+6tP_T'\big).
 }
 \tag{14}
\]
这里 \(Q=1+tK'/K\) 是原 R591 的共同 zeta 对数导数。
(13)–(14) 保两条不同原 charge 及全部分子导数项；不能只保 \(Q_N\) 的已知单位。

## 4. 最后两条 K 系数的完整矩阵

写 \(K=\sum k_nt^n\)，并令
\[
 K^-=\pi_{N-1}K=\sum_{n=0}^{N-2}k_nt^n,\qquad
 U=\frac C{H^2}.
 \tag{15}
\]
在所有以下式子中，\(K^-\) 是实际 \(K\) 的截断。
把最后两项暂时列出，仅用于一个有限多项式恒等式。

若 \(W(0)=1\)、\(a\in\mathcal O\)，且全部所需二项式分母整，则 \(N\ge3\) 给
\[
 [t^N]K^aW
 =a k_N+a\big((a-1)k_1+W_1\big)k_{N-1}
   +[t^N](K^-)^aW .
 \tag{16}
\]
证明：在 \(K=K^-+k_{N-1}t^{N-1}+k_Nt^N\) 中，两个尾项的二次乘积次数至少 \(2N-2>N\)；一次项只读取 \((K^-)^{a-1}W\) 的常数和一次系数，分别为 \(1\) 与 \((a-1)k_1+W_1\)。这证明全式，不把 \(k_{N-1},k_N\) 视作可自由改变的真实来源。

由 (3)、(5)、(6)，
\[
 U_1=-\frac5{14},\quad (P_SU)_1=-\frac{111}{14},
 \quad (P_TU)_1=-\frac{1119}{14}.
\]
于是原两行是
\[
 \boxed{
 A_{34}=\frac{17}3
    \left(k_N-\frac{2057}{210}k_{N-1}\right)+r_{34},
 \quad r_{34}=[t^N](K^-)^{17/3}P_SU,
 }
 \tag{17}
\]
\[
 \boxed{
 A_{72}=12
    \left(k_N-\frac{5903}{70}k_{N-1}\right)+r_{72},
 \quad r_{72}=[t^N](K^-)^{12}P_TU.
 }
 \tag{18}
\]
而 (11) 给
\[
 \boxed{
 \mathfrak c_4=k_N-\frac12k_{N-1}+l_4,\qquad
 \mathfrak c_1=k_N-\frac3{14}k_{N-1}+l_1,
 }
 \tag{19}
\]
其中 \(l_4=[t^N]K^-C\)、\(l_1=[t^N]K^-H^3\)。

(17)–(18) 的最后两系数矩阵行列式为
\[
 \frac{17}3\cdot12
 \left(-\frac{5903}{70}+\frac{2057}{210}\right)
 =-\frac{76024}{15}
 =-\frac{8\cdot13\cdot17\cdot43}{15}.
 \tag{20}
\]
(19) 的行列式为 \(2/7\)。
在 (1) 的每个惰性素数，两者都是单位：
\(7,13,43\) 均是分裂素数，十七已由 \(p\ge23\) 排除。
没有新加一个未支付的同余 ray。

## 5. 四行之间的固定单位比较及全部残差

消去 (17)–(19) 中相同的两个尾系数，得到
\[
 \boxed{
 \begin{pmatrix}A_{34}\\ A_{72}\end{pmatrix}
 =
 \mathsf M
 \begin{pmatrix}\mathfrak c_4\\ \mathfrak c_1\end{pmatrix}
 +
 \begin{pmatrix}\mathfrak R_{34}\\ \mathfrak R_{72}\end{pmatrix},
 \qquad
 \mathsf M=
 \begin{pmatrix}
 17\cdot503/45&-17\cdot488/45\\
 12\cdot1472/5&-12\cdot1467/5
 \end{pmatrix}.
 }
 \tag{21}
\]
两个完整残差准确为
\[
 \boxed{
 \mathfrak R_{34}
 =[t^N]\left\{
 (K^-)^{17/3}P_SU
 -\frac{17}{45}K^-(503C-488H^3)
 \right\},
 }
 \tag{22}
\]
\[
 \boxed{
 \mathfrak R_{72}
 =[t^N]\left\{
 (K^-)^{12}P_TU
 -\frac{12}{5}K^-(1472C-1467H^3)
 \right\}.
 }
 \tag{23}
\]
因此这些残差只使用 \(k_0,\ldots,k_{N-2}\) 以及原固定 \(H,C,P_S,P_T\) 的整截断。它们不使用 \(k_{N-1}\) 或 \(k_N\)，也不是另加的自由变量。

准确行列式为
\[
 \boxed{
 \det\mathsf M=-\frac{266084}{15}
 =-\frac{4\cdot7\cdot13\cdot17\cdot43}{15}
 \in k^\times .
 }
 \tag{24}
\]
例如第一归一行的两个系数来自
\[
 \frac{503}{15}+\left(-\frac{488}{15}\right)=1,\qquad
 -\frac12\frac{503}{15}
 -\frac3{14}\left(-\frac{488}{15}\right)
 =-\frac{2057}{210};
\]
第二行同样由 \(1472/5,-1467/5\) 给出。这也核定 (21) 的全部符号。

(21) 是四条**实际**来源系数之间的恒等式；可逆性只说明两种尾系数坐标在保留残差后等价。不能删除 (22)–(23)，再把它写成两个原行与两个 forcing 的齐次等价。

## 6. 原完整算术同时失败真正给出的条件

R303/R402/R409 的原完整 Selmer 比较和准确 Gaussian 首层给：
在共同好惰性范围，
\[
 J'_{34,p}(0)=J'_{72,p}(0)=0
 \ \Longrightarrow\ A_{34}=A_{72}=0 .
 \tag{25}
\]
固定 \(b\) 和物理 \(E_{24}\) 的同源缩放只乘已经支付的单位，所以 (25) 在 (4) 的共同 frame 中有效。

把 (25) 代入真实 (21)，所得准确输入是
\[
 \boxed{
 \begin{pmatrix}\mathfrak c_4\\ \mathfrak c_1\end{pmatrix}
 =-\mathsf M^{-1}
 \begin{pmatrix}\mathfrak R_{34}\\ \mathfrak R_{72}\end{pmatrix}.
 }
 \tag{26}
\]
在这个**同时失败的假设内**，还有
\[
 (\mathfrak c_4,\mathfrak c_1)=(0,0)
 \quad\Longleftrightarrow\quad
 (\mathfrak R_{34},\mathfrak R_{72})=(0,0).
 \tag{27}
\]
本篇没有证明 (22)–(23) 在实际递推下为零，也没有证明它们不可能满足 (26)。
因此它并未支付原中央失败到 R592 两 forcing 同零的桥。
R592 的 \(\Psi_5\) 本身杀原 \(S,T\)，这一事实也不能代替 (26) 的两份残差。

同样，R591 的下一共振 \(pk_s\) 或 \(Q_N\) 已知为单位，不能只保它在 (13)–(14) 中的单独贡献；其它实际整卷积仍在。
(20)、(24) 的单位行列式也没有把满足固定递推的 \(k_n\) 变成自由参数。

下一实际接口是 (22)–(26) 的**指定**残差及其与 R589 原首极部、完整 addition 整卷积或原全部 jet 的关系。
全部高权 Newton 条件仍按 R303/R402 保留；本篇只运输它们的首层必要条件，不把首层零等同于完整失败。
主目标尚未完成。

## 直接依赖

- [R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)：两个完整原分子、\(T=SH_{38}\)、物理单位与原六 sigma 身份。
- [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)、
  [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)：两条原完整算术桥、Gaussian 及全部 Newton 尾。
- [R409](R409-two-actual-sources-shared-first-diagonal-recurrence.md)：首对角的整性、来源身份及原中央失败的必要条件。
- [R591](R591-original-inert-forcing-in-one-parameter-and-exact-resonance.md)：本篇共同 \(K,H,C,Q\)、单位分母递推和两个指定 forcing。

本篇是全参数有限恒等式与留数证明，没有新增素数扫描。
