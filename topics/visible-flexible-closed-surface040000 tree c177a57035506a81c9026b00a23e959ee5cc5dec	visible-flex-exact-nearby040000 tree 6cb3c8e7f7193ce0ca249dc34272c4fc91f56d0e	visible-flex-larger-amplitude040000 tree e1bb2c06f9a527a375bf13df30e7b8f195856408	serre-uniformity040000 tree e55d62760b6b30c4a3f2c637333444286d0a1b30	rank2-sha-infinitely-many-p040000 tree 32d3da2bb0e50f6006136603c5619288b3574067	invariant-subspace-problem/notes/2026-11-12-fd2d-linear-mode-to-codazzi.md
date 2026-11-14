# 完整线性位移模到 Codazzi/log 变量的准确一阶转换

2026-11-12，root，服务新强目标的非圆分支初猜；接 R116、R117。

本 note 给解析恒等式。实际 v4 全段放大由另名有限线性轨道计算，
不能只由 cut 的高度 gain 推断近水平区的曲率扰动大小。
小幅线性解不等于大幅非线性闭核，也不直接支付 R119 的残差界。

## 1. 同一 g 的旋转背景与线性位移

取原固定 \(g=ds^2+a(s)^2du^2\)，设 \(|a'|<1\)、
\(b=\sqrt{1-a'^2}>0\)。旋转背景为

\[
X_0=a(s)e_r(u)+z(s)e_z,\qquad z'=b,
\]
\[
e_1=a'e_r+be_z,\quad e_2=e_\theta,\quad
N=e_1\times e_2=-be_r+a'e_z.
\]

它的正交第二基本形式是
\(n_0=b/a\)、\(m_0=0\)、\(l_0=-a''/b\)。
对一个整数角模 k≥2，取实际线性位移

\[
V=f(s)\cos(ku)e_r-\frac{f(s)}k\sin(ku)e_\theta
+g(s)\cos(ku)e_z.
\tag{1}
\]

线性等距条件为

\[
f'=-\frac{(k^2-1)a'f+k^2bg}{a},\qquad
g'=\frac{(k^2-1)a'^2f/b+k^2a'g}{a}.
\tag{2}
\]

这是当前 profile 的 `Candidate.linear` 所用的 f、g 约定。
中央柱若取 f(0)=ε、g(0)=0，则一阶长轴支持增加 ε、短轴支持减少 ε。
这只是小 ε 的导数，不能对目标大幅度直接作线性外推。

## 2. 实际第二基本形式的线性化

由 (1)，

\[
V_u=-\sin(ku)\left\{\frac{k^2-1}{k}f e_r+kg e_z\right\}.
\]

线性等距使 \(\delta e_1=V_s\)、\(\delta e_2=V_u/a\)。
因此实际单位法向的一阶变化为

\[
\delta N=-g'\cos(ku)e_r+f'\cos(ku)e_z
+\frac{ka'g-(k^2-1)bf/k}{a}\sin(ku)e_\theta.
\tag{3}
\]

对 \(n=X_{uu}\cdot N/a^2\) 求导，得到

\[
\delta n=
\frac{(k^2-1)bf-k^2a'g+ag'}{a^2}\cos(ku)
=\frac{(k^2-1)f}{a^2b}\cos(ku).
\tag{4}
\]

最后一步代入 (2)，并使用 \(a'^2+b^2=1\)。
类似地，对 \(m=X_{su}\cdot N/a\) 求导，得到

\[
\boxed{\delta m=-\frac{k(k^2-1)}{a^2}
\left(\frac{a'f}{b}+g\right)\sin(ku).}
\tag{5}
\]

等价地，利用 f 的方程，

\[
\delta m=\frac{k^2-1}{kab}(f'-cf)\sin(ku),\qquad c=a'/a.
\]

这些是由**实际位置和单位法向**求出的导数，未把辅助 frame 的某个分量当成第二基本形式。
共同 g 的线性 Gauss 方程还给
\(n_0\delta l+l_0\delta n=0\)。

## 3. 正值变量中的分支初猜

令

\[
n=n_0e^\eta,\qquad m=n_0\zeta,
\quad \chi=K/n_0^2,\quad K=-a''/a.
\]

一阶的 \(\eta=\delta n/n_0\)、\(\zeta=\delta m/n_0\) 因而是

\[
\boxed{\eta_{lin}=\frac{(k^2-1)f}{ab^2}\cos(ku),\qquad
\zeta_{lin}=-\frac{k(k^2-1)}{ab}
\left(\frac{a'f}{b}+g\right)\sin(ku).}
\tag{6}
\]

特别地 k=2 时，两个振幅为 \(3f/(ab^2)\) 与
\(-6(a'f/b+g)/(ab)\)。
若 (2) 是 f(0)=1 的规范化轨道，乘一个真实小 ε 才是小幅初猜。
要让整段的线性 log 扰动有预定大小，必须先计算 (6) 的**全段**振幅；
近水平 b 很小时，cut 的小高度输出不能控制其中的 \(b^{-2}\) 放大。

由 R116 的方程准确换元得到稳定同 g 的非线性形式

\[
\eta_s=e^{-\eta}D\zeta+c\{\zeta^2e^{-2\eta}
+\chi\operatorname{expm1}(-2\eta)\},
\]
\[
\zeta_s=e^{-\eta}\{2\zeta D\zeta-(\zeta^2+\chi)D\eta\}
-c(\chi+1)\zeta,\qquad D=a^{-1}\partial_u.
\tag{7}
\]

推导只用 \(n_0'/n_0=c(\chi-1)\)，因此不要求 a 的三阶导数。
η=ζ=0 是准确旋转背景；expm1 写法避免把两个大 χ 项先相减。
若用动态计算角 u=U(s,ξ)，把 D 换为 \((aU_\xi)^{-1}\partial_\xi\)，
并在两式各加 \((U_s/U_\xi)\partial_\xi\) 的漂移。

在线性层，令 \(\eta=A(s)\cos(ku)\)、\(\zeta=B(s)\sin(ku)\)，则

\[
\binom{A'}{B'}=
\begin{pmatrix}-2c\chi&k/a\\k\chi/a&-c(\chi+1)\end{pmatrix}
\binom AB.
\tag{8}
\]

(6) 与 (2) 满足这个相同线性系统。它可以直接用来生成完整 n,m 分支初猜，
不必先把数千个位置/标架变量塞进非线性求解未知量。

## 4. 与实际尾端口的一阶符号对应

在 r=a 的 cut，令 v=a′<0，物理上半高度模为 gk，
其有限线性尾方向满足 \((g_k)_r=D_k g_k\)。
R117 的上半法向约定是 \(N_z=v<0\)。
对 height-jet 公式在旋转背景求真实一阶导数，得到

\[
\delta n=\frac{rD_k-k^2}{r^2v}g_k\cos(ku),\qquad
\delta m=-\frac{k(rD_k-1)}{r^2}g_k\sin(ku).
\tag{9}
\]

例如 n 的公式可直接从
\(n=(H_{uu}/r^2+v^2H_r/r)/N_z\) 求导：
背景 \(H_r=-w\)、\(v=-1/\sqrt{1+w^2}\)、\(b=-vw\)，
且 \(\delta N_z=vw\,\delta H_r\)。合并分子和法向分母的导数后，
\(\delta n=(r\delta H_r-k^2g_k)/(r^2v)\)。
m 背景为零，直接得到 (9) 的第二式。

尾方向的位移关系是
\(f/g_k=-w(rD_k-k^2)/(k^2-1)\)。代入 (4)–(5)，
利用 b=−vw，准确复现 (9)。
如果程序未知量是 worker 的高度 \(h_k=-g_k\)，两式整体反号；
不能把同一系数同时解释为 worker 高度和上半真实 z 高度。

(9) 可作纯线性分支初猜的端口列。把线性 H/Hr/Hrr 代入完整平方根公式
还会引入特定的二次及更高项；这些项不是实际 nonlinear DN 的返回，
不得借它们声称端口已非线性闭合。真正非线性阶段仍消费 R117 的实际 worker 包。

## 5. 对当前工作的具体限制

有限线性尾图只提供初猜和线性方向。后续实际解仍需真实 nonlinear DN、
完整未省略的 cut 残差、准确中央闭曲线、同 g 的实际加密、连续 metric 及全部几何条件。
若增加一个明确的 profile 设计参数以固定非圆幅度，须给新候选名字；
最终确定 g 后的误差加密才能算同 g 收敛。
物理 profile 的改变、算法坐标的改变和单纯增加表示分辨率必须区分。
