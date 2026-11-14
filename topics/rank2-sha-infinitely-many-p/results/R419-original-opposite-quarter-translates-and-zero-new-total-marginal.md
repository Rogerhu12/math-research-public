# R419 — 原相反四挠平移的完整消失与新增总输出零边际

日期：2026-11-14。**状态：已证明。** 对 R416 的原两条来源 $S,L$，
同一真实 $Y$ 符号反射后出现的新总输出来源准确恒等于零：
$$
U(z)=\frac14\sum_{t\in E[4]}S_{-t}(z)L_t(z)
      -\frac12\sum_{t\in E[2]}S_{-t}(z)L_t(z)=0.
$$
本篇分别证明非二挠四挠和、完整二挠和都为零。
证明给出 canonical 平移常数、完整有理商及因式恒等式，不使用采样、
数值近似或“质量零所以来源零”。因此新增总输出的任何完整连续测试
都为零；任意隐藏受限域仍不因此自动为零。主目标尚未完成。

## 1. 两条实际来源、真实 lift 和结论

保持 R398、R413、R416 的同一物理曲线
$E_b:y^2=x^3+b$、$b=17$、原微分、sigma 和普通周期。
写 $X=x^3$，则
$$
\begin{aligned}
S&=\sigma^{34}s_b(x),\\
s_b(x)&=x^2(X+b)(X-8b)
                  (X^2-4bX/7+16b^2/7),\\
L&=\sigma^{38}l_b(x),\\
l_b(x)&=x(X^2+20bX-8b^2)(X+4b)
                    (X^3-96bX^2+48b^2X+64b^3),\\
T&=SL.
\end{aligned}
\tag{1}
$$
这是首项一的原 $S,T$ 和质量一的原 $L$，不是相同 degree 的新候选。
采用 R416 的原对称 lift
$$
F_t(z)=\mathsf T_t^{(\deg F)}F(z)
       =e^{-\deg(F)\eta_t(z+t/2)}F(z+t).
\tag{2}
$$

**定理。** 在上述原规范中，完整函数身份为
$$
\boxed{\sum_{t\in E[4]\setminus E[2]}S_{-t}L_t=0,}
\tag{3}
$$
$$
\boxed{\sum_{t\in E[2]}T_t=0.}
\tag{4}
$$
二挠时 $S_{-t}=S_t$，且 $S_tL_t=T_t$。因此
$$
\boxed{
U=\frac14\sum_{t\in E[4]\setminus E[2]}S_{-t}L_t
             -\frac14\sum_{t\in E[2]}T_t=0.}
\tag{5}
$$
还直接得到另一份精确来源恒等式
$$
\boxed{U^{\rm core}=-\frac14\sum_{t\in E[4]}S_{-t}L_t=0.}
\tag{5a}
$$
这两份权不能混淆：后续实际 $Y$-core 在非二挠四挠点带有额外
中心负号，因此会使用 (5a)。本篇分别支付 (3)、(4)，使两份总输出
都确实为零，而不需要忽略那个中心符号。

对四挠 $t$，$S_{-t}$、$L_t$ 单独可带平坦 twist；二者乘积的
twist 参数为 $-34t+38t=4t\in\Lambda$，所以乘积恰在原 degree72
线丛中。按 (2) 检查一个周期的交叉指数，它是
$\eta_\ell(4t)-\eta_{4t}\ell\in2\pi i\mathbf Z$，因而确实消失。
改变四挠代表也不改变该乘积：总 degree 为 $72$，而 $72/4=18$
为偶数，原中心相位为一。下面始终计算这个完整乘积，不单独去掉
任何平坦 twist。

## 2. 四挠 canonical 常数与完全有理的乘积

对 $t\in E[4]\setminus E[2]$，置
$$
e=x(t),\quad f=y(t),\quad h=x(2t),\quad h^3=-b,
$$
$$
c_t=e^{-\eta_t t/2}\sigma(t),\qquad
\sigma_t(z)=e^{-\eta_tz}\frac{\sigma(z+t)}{\sigma(t)}.
$$
设 $x=x(z)$、$y=y(z)$，真实加法式给
$$
x_+=x(z+t)=\frac{e x^2+e^2x+2b-2fy}{(x-e)^2},\qquad
x_-=x(z-t)=\frac{e x^2+e^2x+2b+2fy}{(x-e)^2},
\tag{6}
$$
以及
$$
\sigma_{-t}(z)\sigma_t(z)=(x-e)\sigma(z)^2.
\tag{7}
$$
定义有理函数
$$
R_t(z)=\frac{\left(y+f+\frac{3e^2}{2f}(x-e)\right)^2}{x-h}.
\tag{8}
$$
其分子来自 $-t$ 的切线：该切线除子为
$2[-t]+[2t]-3[O]$。因为 $2t$ 是二挠，(8) 的除子恰为
$4[-t]-4[O]$；在 $z=0$ 的首系数为一。
$\sigma_t^4/\sigma^4$ 有相同除子及首系数，故准确有
$$
\boxed{\sigma_t^4/\sigma^4=R_t.}
\tag{9}
$$

R416 的半周期归一给 $c_{2t}^4=(3h^2)^{-1}$。
将真正的 $(\mathsf T_t^{(4)})^2=\mathsf T_{2t}^{(4)}$ 作用于
$\sigma^4$，再在零处取值，得到
$c_t^8R_t(t)=c_{2t}^4$。由 $R_t(t)=4f^2/(e-h)$，完整常数为
$$
\boxed{c_t^8=\frac{e-h}{12h^2f^2},\qquad
 c_t^{72}=\left(\frac{e-h}{12h^2f^2}\right)^9.}
\tag{10}
$$
没有选择一个不明的四次根或八次根。

由于 $c_{-t}=-c_t$、两个原 degree 都为偶数，(7)、(9) 将实际
相反平移乘积完全写为
$$
\boxed{
\frac{S_{-t}(z)L_t(z)}{\sigma(z)^{72}}
=\left(\frac{e-h}{12h^2f^2}\right)^9
 (x-e)^{34}R_t(z)\,s_b(x_-)l_b(x_+).}
\tag{11}
$$
这是本篇求和的全函数输入。

## 3. 一条二挠纤维上四点的完整因式

先在 $b=1$ 模型计算，取 $h=-1$。
四个 $[2]$ 原像准确由
$$
e=-q,\quad q^2-2q-2=0,\quad f^2=-6q-3=:F
\tag{12}
$$
及两种 $f$ 符号给出。它们都不是二挠；$F$ 在两条 $q$ 嵌入中的
范数为 $-27$，故没有零分母。
令 $Q(x)$ 是这四个点的 (11) 之和。

**四点完整式。** 置
$$
X=x^3,\qquad R(X)=X^2+20X-8,
$$
$$
V(X)=X^4-536X^3-1344X^2-2048X-512.
$$
则
$$
\boxed{
Q(x)=\frac2{189}(X-8)(X+1)R(X)^2V(X)
             \left[x^2(X-8)-8x(X+1)\right].}
\tag{13}
$$
尤其它的全部幂次都等于 $1$ 或 $2\pmod3$；这不是只检查原点
或前若干矩。

下面给出 (13) 的明确有理恒等式及其完整计算规则。
在二次商环
$$
\mathbf Q(q)[x,\tau]/\bigl(\tau^2-F(x^3+1)\bigr)
$$
中置
$$
d=(x+q)^2,\quad a=-qx^2+q^2x+2,\quad
n_\pm=a\pm2\tau,\quad
c=F+\tfrac32q^2(x+q),
$$
$$
\mathcal S=d^{14}s_1(n_+/d),\qquad
\mathcal L=d^{19}l_1(n_-/d).
\tag{14}
$$
二者是显示商环中的多项式。将任意元素唯一写成 $A(x)+\tau B(x)$，
记其 $A(x)$ 为 $\operatorname{ev}_\tau$。
由 (6)、(8)、(10)，两种 $f$ 的完整和正是
$$
Q_q(x)=
\frac{2}{F}\left(\frac{1-q}{12F}\right)^9
\frac{\operatorname{ev}_\tau\bigl((\tau+c)^2\mathcal S\mathcal L\bigr)}
     {(x+q)^{32}(x+1)}.
\tag{15}
$$
分母指数 $32$ 是原 $34-2\cdot14-2\cdot19=-32$，不是事后
补出的归一。按 $q^2=2q+2$ 逐次乘法，(15) 的分子对显示分母
作整除，余数准确为零，商的次数为 $35$。
再将 $q$ 换成 $2-q$ 并相加，完整结果恰为 (13)。
即本篇使用的明确多项式身份是
$$
\boxed{Q_q(x)+Q_{2-q}(x)=Q(x)\text{，其中右边为 (13)。}}
\tag{16}
$$
式 (14)、(15) 提供全部输入，(13) 提供完整因式答案；附带脚本在
$\mathbf Q(\sqrt3)[x,\tau]/(\tau^2-F(X+1))$ 中直接相乘、整除并
逐系数核定 (16)。没有任何插值点或截断尾。

### 3.1 三个二挠纤维的真实求和

原 $S,L$ 都满足 $F(\omega z)=F(z)$。同一个 canonical lift 因而有
$F_{\omega t}(z)=F_t(\omega^{-1}z)$；degree72 的 sigma frame 在
这个旋转下没有相位。
三个非零二挠点的上述四点和，故分别是
$Q(x),Q(\omega x),Q(\omega^2x)$。
(13) 完全显式地给
$$
Q(x)+Q(\omega x)+Q(\omega^2x)=0.
\tag{17}
$$
乘回 $\sigma^{72}$ 就证明 (3)，包括全部十二个非二挠四挠点。

## 4. 原二挠平移和也完整为零

仍在 $b=1$ 模型，写
$$
\begin{aligned}
P_T(X)={}&\frac17X(X-8)(X+1)(X+4)R(X)\
&\quad\cdot(7X^2-4X+16)(X^3-96X^2+48X+64),
\end{aligned}
\tag{18}
$$
所以原 $T=\sigma^{72}P_T(x^3)$。
对 $e=x(t)=-1$ 的二挠点，R416 的准确半周期常数和横坐标式给
$$
\frac{T_t(z)}{\sigma(z)^{72}}
=\frac{(x+1)^{36}}{3^{18}}
       P_T\left(\left(\frac{2-x}{x+1}\right)^3\right)=:H(x).
\tag{19}
$$
它是多项式，因为原 $P_T(x^3)$ 的次数为 $33<36$。

为保留所有角列，定义
$$
C_5(X)=X^5+140X^4-2528X^3-5984X^2-6016X-512,
$$
$$
C_7(X)=X^7-200X^6-15072X^5-47296X^4
 -372736X^3-577536X^2-210944X-32768,
$$
$$
H_1(X)=-\frac2{189}(X-8)(X+1)R(X)(7X^2-4X+16)C_5(X),
$$
$$
H_2(X)=\frac1{189}(X-8)(X+1)R(X)C_7(X).
$$
完整的有理多项式身份为
$$
\boxed{H(x)=-\frac13P_T(X)+xH_1(X)+x^2H_2(X).}
\tag{20}
$$
它直接由 (18)、(19) 的有限二项展开得到，附带脚本逐系数证明整个
(20)，不是只核查十三个目标点。
三条实际半周期的和于是准确为
$$
H(x)+H(\omega x)+H(\omega^2x)=-P_T(X).
\tag{21}
$$
乘回原 sigma frame，非零二挠点的平移和等于 $-T$；再加入原点项
$T$，得到 (4)。

## 5. 返回同一物理曲线与所有完整输出测试

从 $E_1$ 返回 $E_b$ 的同源缩放为
$$
z'=b^{1/6}z,\quad x_b=b^{1/3}x_1,\quad
\sigma_b(z)=b^{-1/6}\sigma_1(z').
$$
由 (1)，准确有
$$
S_b(z)=b^{-1}S_1(z'),\qquad L_b(z)=L_1(z'),\qquad
T_b(z)=b^{-1}T_1(z').
$$
canonical lift 与这个缩放相容：$t'=b^{1/6}t$，准周期相应缩放，
原指数在两边完全相等。因此 (3)、(4) 都带相同整体 $b^{-1}$
返回原 $b=17$ 模型，零恒等式不依赖辅助选取的六次根。
这个过程没有改动 R398 的实际 $E_{24}$ 物理标量。

记 R416(11) 的实际 $(Y,x_2)$ 联合为 $\widetilde F$。
因为 $S$ 是偶来源，原 lift 直接给 $S_t(-y)=S_{-t}(y)$。
所以普通的真实坐标反射 $(Y,x_2)\mapsto(-Y,x_2)$ 的来源准确是
$$
F^{\mathrm{ref}}(y,v)
=\frac14\sum_{t\in E[4]}S_{-t}(y)L_t(v)
 -\frac12\sum_{t\in E[2]}S_{-t}(y)L_t(v).
\tag{22}
$$
即 $F^{\mathrm{ref}}(y,v)=\widetilde F(-y,v)$；这是一个明确的整
联合测度推前，不依赖先将反射认成 $Y$-core。
设置 $y=v=z$ 是同一个真实总输出 $W=Y+x_2$ 的推前。
(5) 及 Amice 单射因而给出完整测度身份
$$
\boxed{W_*\nu_{F^{\mathrm{ref}}}=0.}
\tag{23}
$$
原联合的构造和整性沿 R413、R416，四挠单项本身的平坦 twist
不被单独丢掉。由 (23)，任意连续 $\varphi(W)$ 的完整积分都为零，
涵盖全部 tame、单位／非单位、任意输出环带及其中央导数。
这比只知道质量 $U(0)=0$ 强，但仍不是把另加隐藏条件后的积分
自动设零。实际 $Y$-core 的新联合使用 (5a) 的全部四挠负权；
同一证明也支付它的完整总输出零，完整算子与中央运输由后续原 core
接口另行识别。

## 6. 精确证书与依赖

`scripts/check-original-opposite-quarter-translate-zero.py` 使用 SymPy
的精确 $\mathbf Q(\sqrt3)$ 多项式环。它从 (1)、(6)、(10) 的
原输入构造 (14)、(15)，验证整除余数零和完整 (13)、(20)，并
输出全部有理系数。没有采样、浮点、目标素数扫描或未知中央输入。
同名 JSON 保存此次输出。

- [R398：原 $S,T,L$ 来源与四挠除子](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。
- [R413：同一完整联合和实际总输出 core](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R416：四挠 lift、半周期归一与原两边际](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
