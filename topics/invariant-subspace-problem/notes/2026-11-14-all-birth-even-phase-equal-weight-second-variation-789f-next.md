# 任意偶数位数的真实相位二阶缺陷：两条跨出生映射的正平方和

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：本文证明任意偶数位数、整个临界 primitive 源上的完整二阶算子恒等式，并给出固定非退化方向的实际局部严格相位界。** 局部半径允许依赖位数和方向。二阶项退化时，本文不宣称它能支付更高阶项，也不据此宣称整个等权邻域或全部正权的统一界。

## 1. 固定源、实际权变形与物理酉归一

固定 \(M=2s\)、\(s\ge1\)，以及实向量 \(x=(x_i)_{i=1}^{2s}\)，满足
\[
\sum_i x_i=0.
\tag{1.1}
\]
对充分小的实 \(\varepsilon\)，令
\[
z_i(\varepsilon)=1+\varepsilon x_i>0,
\qquad b_i(\varepsilon)=\sqrt{z_i(\varepsilon)}.
\]
定义真实正权删除、对偶创建
\[
d_\varepsilon=\sum_i b_i(\varepsilon)E_i,
\qquad e_\varepsilon=\sum_i b_i(\varepsilon)^{-1}E_i^*.
\]
无权时记 \(d_0=\sum_iE_i\)、\(e_0=d_0^*=\sum_iE_i^*\)，并置
\[
U_0=\ker d_0\cap H_s,\qquad
V_0=\ker d_0\cap H_{s-1},\qquad
W_0=\ker d_0\cap H_{s-2}.
\tag{1.2}
\]
\(s=1\) 时 \(W_0=0\)，含它的映射一并为零。

在第 \(j\) 层令
\[
D_j(\varepsilon)e_I=
\left(\prod_{i\in I}b_i(\varepsilon)\right)e_I,
\qquad \pi(\varepsilon)=\prod_i z_i(\varepsilon).
\]
对角去权满足
\(d_\varepsilon|_{H_j}=D_{j-1}^{-1}d_0D_j\)。因此同一个固定源映射
\[
\mathcal E_\varepsilon=D_{s-1}(\varepsilon)^{-1}|_{V_0}
:V_0\to V_\varepsilon:=\ker d_\varepsilon\cap H_{s-1}
\tag{1.3}
\]
是双射。其物理度量是
\[
H_\varepsilon=\mathcal E_\varepsilon^*\mathcal E_\varepsilon,
\qquad
\mathcal U_\varepsilon=\mathcal E_\varepsilon H_\varepsilon^{-1/2}.
\tag{1.4}
\]
\(\mathcal U_\varepsilon\) 是从原物理 \(V_0\) 到 \(V_\varepsilon\) 的酉同构；本文最后的算子展开使用这个酉归一。

在真实变形源上记
\[
G_\varepsilon=\Gamma_{1,s-1},\quad
L_\varepsilon=\Gamma_{2,s-1},\quad
A_{0,\varepsilon}=e_\varepsilon^*|_{\ker d_\varepsilon\cap H_s},
\]
\[
H_{0,\varepsilon}=G_\varepsilon^{-1}L_\varepsilon
                  -2G_\varepsilon-A_{0,\varepsilon}A_{0,\varepsilon}^*,
\qquad
\Phi_\varepsilon=H_{0,\varepsilon}^*L_\varepsilon^{-1}H_{0,\varepsilon}.
\tag{1.5}
\]
所有 \(\Gamma\) 都是完整层 \(d_\varepsilon^j/j!\) 的最小逆后压 primitive 的 Gram。

## 2. 两条无权真实跨出生映射与主结论

令
\[
d_x=\sum_i x_iE_i,\qquad
B_x=d_x|_{V_0}:V_0\to W_0,
\qquad S_x=P_{U_0}d_x^*|_{V_0}:V_0\to U_0.
\tag{2.1}
\]
\(B_x\) 的值域在 \(W_0\)，因为 \([d_0,d_x]=0\)。\(S_x\) 是同一物理中层中到真正最高 primitive 源的正交投影。它们不是按某个非正交去权坐标取出的伪伴随。

**定理 2.1（完整二阶平方和）。** 在 \(V_0\) 的算子范数下，
\[
\boxed{
I_{V_0}-\mathcal U_\varepsilon^*\Phi_\varepsilon\mathcal U_\varepsilon
=\varepsilon^2\left(\frac14B_x^*B_x+\frac12S_x^*S_x\right)
 +O_x(\varepsilon^3).
}
\tag{2.2}
\]
余项估计对固定的有限 \(s,x\) 成立；没有声称其常数对 \(s,x\) 一致。

为给出可检查的非退化条件，定义中央占据算子
\[
X_s=\sum_i x_i n_i\quad\hbox{于 }H_s,
\qquad
m(x)=\min_{|I|=s}\left|\sum_{i\in I}x_i\right|.
\tag{2.3}
\]
下文同时证明
\[
\boxed{
\frac38\,e_0^*X_s^2e_0|_{V_0}
\preceq \frac14B_x^*B_x+\frac12S_x^*S_x
\preceq\frac12\,e_0^*X_s^2e_0|_{V_0}.
}
\tag{2.4}
\]

**推论 2.2。** 如果 \(m(x)>0\)，则
\[
\frac14B_x^*B_x+\frac12S_x^*S_x\succeq\frac34m(x)^2 I_{V_0}.
\tag{2.5}
\]
因此存在依赖固定 \(s,x\) 的 \(\varepsilon_0>0\)，使所有
\(0<|\varepsilon|<\varepsilon_0\) 都有真正的全源严格界
\[
\Phi_\varepsilon\prec I_{V_\varepsilon}.
\tag{2.6}
\]
更一般地，只要 (2.2) 的二次系数正定，同一局部结论就成立；\(m(x)>0\) 是一个充分条件，不是必要条件。

## 3. 固定源上的四个完整形式

下面所有压缩都在固定无权源 \(V_0\) 上，记其正交投影为 \(P_0\)。在完整 \(H_{s-1}\) 上定义
\[
K(\varepsilon)=d_0D_s(\varepsilon)^2e_0.
\tag{3.1}
\]
它严格正，因为中层删除 \(d_0:H_s\to H_{s-1}\) 满射。完整第一 Gram 为
\(D_{s-1}^{-1}K(\varepsilon)D_{s-1}^{-1}\)。所以第一真实形式是
\[
g_\varepsilon:=\mathcal E_\varepsilon^*G_\varepsilon\mathcal E_\varepsilon
=P_0K(\varepsilon)^{-1}|_{V_0}.
\tag{3.2}
\]
这是完整逆后再压缩，全部 nuisance 均保留。

真正顶端的补集公式给
\[
\ell_\varepsilon:=\mathcal E_\varepsilon^*L_\varepsilon\mathcal E_\varepsilon
=\pi(\varepsilon)^{-1}P_0D_{s-1}(\varepsilon)^2|_{V_0},
\tag{3.3}
\]
而原源度量是
\[
H_\varepsilon=P_0D_{s-1}(\varepsilon)^{-2}|_{V_0}.
\tag{3.4}
\]

还有一个在本阶计算中很有用的准确对偶形式。令
\(Q_{0,\varepsilon}=P_{V_\varepsilon}e_\varepsilon^*e_\varepsilon|_{V_\varepsilon}\)，则
\[
q_\varepsilon:=\mathcal E_\varepsilon^*Q_{0,\varepsilon}\mathcal E_\varepsilon
=P_0d_0D_s(\varepsilon)^{-2}e_0|_{V_0}
=\pi(\varepsilon)^{-1}P_0K(\varepsilon)|_{V_0}.
\tag{3.5}
\]
最后一个等式使用中央补集 \(\mathfrak c\) 的两个准确身份
\[
\mathfrak cD_s^2\mathfrak c=\pi D_s^{-2},
\qquad \mathfrak c e_0|_{V_0}=(-1)^{s-1}e_0|_{V_0}.
\]
第二式是无权 Boolean 的最高塔补集关系；等价地，
\(\mathfrak c|_{V_0}=(-1)^{s-1}e_0^2/2\)，再作一次删除即可。

真实分解 \(e_\varepsilon|_{V_\varepsilon}=2\mathcal J_{1,s-1}+A_{0,\varepsilon}^*\) 进一步给
\[
Q_{0,\varepsilon}=4G_\varepsilon+A_{0,\varepsilon}A_{0,\varepsilon}^*.
\tag{3.6}
\]
因此相位中用的是
\(H_{0,\varepsilon}=G_\varepsilon^{-1}L_\varepsilon+2G_\varepsilon-Q_{0,\varepsilon}\)。

## 4. 无权中央的三塔身份

在每个层上写
\[
X_j=\sum_i x_i n_i,
\quad Y_j=\sum_i x_i^2 n_i,
\quad X=P_0X_{s-1}|_{V_0},
\quad Y=P_0Y_{s-1}|_{V_0},
\quad \tau=\sum_i x_i^2.
\tag{4.1}
\]
由 \([d_0,X_j]=d_x\)，有完整正交分解
\[
X_{s-1}|_{V_0}=\iota_{V_0}X+\frac14e_0 B_x.
\tag{4.2}
\]
这里 \(W_0\) 的无权高度为四，故 \(d_0e_0|_{W_0}=4I\)。

又由 (1.1)，
\(d_0d_x^*|_{V_0}=-2X_{s-1}|_{V_0}\)。在中央正交三塔
\(U_0\oplus e_0V_0\oplus e_0^2W_0\) 上逐项匹配删除，得到
\[
d_x^*|_{V_0}
=S_x-e_0X-\frac1{12}e_0^2B_x.
\tag{4.3}
\]
它没有更深分量：\(d_0^3d_x^*|_{V_0}=0\)，而前三塔恰构成中央 \(\ker d_0^3\)。其中
\(d_0e_0|_{V_0}=2I\)、\(d_0e_0^2|_{W_0}=6e_0\)，核对了两个非零系数。

结合 \(X_s e_0=e_0X_{s-1}+d_x^*\)，(4.2)–(4.3) 严格相消为
\[
\boxed{X_s e_0|_{V_0}=S_x+\frac16e_0^2B_x.}
\tag{4.4}
\]
两项落在正交的 \(U_0\) 与 \(e_0^2W_0\)。无权高度四给
\[
\|e_0B_xf\|^2=4\|B_xf\|^2,
\qquad \|e_0^2B_xf\|^2=24\|B_xf\|^2.
\tag{4.5}
\]
故
\[
e_0^*X_s^2e_0|_{V_0}=S_x^*S_x+\frac23B_x^*B_x.
\tag{4.6}
\]
式 (2.4) 现在由两项的非负性直接得出。

## 5. 完整第一逆的二阶展开，不丢低塔

由于每个 \(n_i\) 是占据投影，准确有
\[
D_j^2=I+\varepsilon X_j
       +\frac{\varepsilon^2}{2}(X_j^2-Y_j)+O_x(\varepsilon^3),
\]
\[
D_j^{-2}=I-\varepsilon X_j
       +\frac{\varepsilon^2}{2}(X_j^2+Y_j)+O_x(\varepsilon^3),
\quad
\pi^{-1}=1+\frac{\tau}{2}\varepsilon^2+O_x(\varepsilon^3).
\tag{5.1}
\]
记
\(K=K_0+\varepsilon K_1+\varepsilon^2K_2+O_x(\varepsilon^3)\)。由 (4.4)，
\[
K_0|_{V_0}=2I,\qquad K_1|_{V_0}=e_0B_x,
\qquad K_0|_{e_0W_0}=6I.
\tag{5.2}
\]
所以 \(P_0K_1|_{V_0}=0\)，并且
\[
P_0K_1K_0^{-1}K_1|_{V_0}=\frac23B_x^*B_x.
\tag{5.3}
\]
这个 \(1/6\) 的完整 nuisance 逆是必须保留的；若先把 \(K\) 压到 \(V_0\) 再求逆，就会漏掉 (5.3)。

由 (4.6) 及 \(P_0d_0Y_s e_0|_{V_0}=\tau I\)，有
\[
P_0K_2|_{V_0}
=\frac12S_x^*S_x+\frac13B_x^*B_x-\frac\tau2I.
\tag{5.4}
\]
最后一个占据身份也可直接用 (5.2) 的同一一阶计算，将系数 \(x_i\) 换成 \(x_i^2\)：非零总和只在 primitive 压缩留下 \(\tau I\)。

完整逆的标准二阶乘法恒等式给
\[
g_\varepsilon=\frac12I+\varepsilon^2g_2+O_x(\varepsilon^3),
\quad
\boxed{g_2=\frac1{12}B_x^*B_x-\frac18S_x^*S_x+\frac\tau8I.}
\tag{5.5}
\]
这是 (5.3) 与 (5.4) 合并后的结果。

同时由 (4.2)、(5.1)，四个形式的全部二阶项为
\[
H_\varepsilon=I-\varepsilon X+\varepsilon^2h_2+O_x(\varepsilon^3),
\quad h_2=\frac12(X^2+Y)+\frac18B_x^*B_x,
\]
\[
\ell_\varepsilon=I+\varepsilon X+\varepsilon^2\ell_2+O_x(\varepsilon^3),
\quad \ell_2=\frac12(X^2-Y)+\frac18B_x^*B_x+\frac\tau2I,
\]
\[
q_\varepsilon=2I+\varepsilon^2q_2+O_x(\varepsilon^3),
\quad q_2=\frac13B_x^*B_x+\frac12S_x^*S_x+\frac\tau2I.
\tag{5.6}
\]
所有 \(g_2,h_2,\ell_2,q_2\) 都是同一个固定物理 \(V_0\) 上的自伴算子。

## 6. 物理相位中的精确二阶抵消

将算子拉回 \(\mathcal E_\varepsilon\) 的坐标，记
\[
\mathsf G=H_\varepsilon^{-1}g_\varepsilon,
\quad \mathsf L=H_\varepsilon^{-1}\ell_\varepsilon,
\quad \mathsf Q=H_\varepsilon^{-1}q_\varepsilon,
\quad \mathsf H_0=\mathsf G^{-1}\mathsf L+2\mathsf G-\mathsf Q.
\]
把 (5.5)–(5.6) 按此非交换顺序相乘，得到
\[
\mathsf L=I+2\varepsilon X
 +\varepsilon^2(2X^2-Y+\tfrac\tau2I)+O_x(\varepsilon^3),
\tag{6.1}
\]
\[
\boxed{
\mathsf H_0=I+\varepsilon X
 +\varepsilon^2\left(\frac12X^2-\frac12Y+\frac\tau4I
 -\frac18B_x^*B_x-\frac14S_x^*S_x\right)
 +O_x(\varepsilon^3).
}
\tag{6.2}
\]
在这些坐标中，真正伴随为
\(\mathsf H_0^{*H}=H_\varepsilon^{-1}\mathsf H_0^*H_\varepsilon\)。由于
\(H_\varepsilon=I-\varepsilon X+O(\varepsilon^2)\)，而 (6.2) 的前两阶均自伴且其一次项也是 \(X\)，有
\(\mathsf H_0^{*H}=\mathsf H_0+O_x(\varepsilon^3)\)。这仅是本阶结论，未称 H0 在所有参数下自伴。

因此 (6.1)–(6.2) 的共同差为
\[
\mathsf L-\mathsf H_0\mathsf H_0^{*H}
=\varepsilon^2\left(\frac14B_x^*B_x+\frac12S_x^*S_x\right)
 +O_x(\varepsilon^3).
\tag{6.3}
\]
也可直接乘出
\[
\mathsf H_0^{*H}\mathsf L^{-1}\mathsf H_0
=I-\varepsilon^2\left(\frac14B_x^*B_x+\frac12S_x^*S_x\right)
 +O_x(\varepsilon^3).
\tag{6.4}
\]
最后，物理酉坐标下的相位为
\[
\mathcal U_\varepsilon^*\Phi_\varepsilon\mathcal U_\varepsilon
=H_\varepsilon^{1/2}
 (\mathsf H_0^{*H}\mathsf L^{-1}\mathsf H_0)
 H_\varepsilon^{-1/2}.
\]
\(H_\varepsilon^{\pm1/2}=I+O_x(\varepsilon)\)，所以该共轭不改变 (6.4) 的二次系数，证明 (2.2)。

## 7. 非退化方向的局部界及其量词

若 \(m(x)>0\)，则完整中央对角算子满足 \(X_s^2\succeq m(x)^2I\)。由
\(e_0^*e_0|_{V_0}=2I\) 及 (2.4)，立即得 (2.5)。

固定 \(s,x\) 后，所有有限矩阵及完整逆在 \(\varepsilon=0\) 的一个邻域内解析，故 (2.2) 的余项范数被 \(M_x|\varepsilon|^3\) 控制。若二次系数的最小特征值为 \(\lambda_x>0\)，再缩小邻域使
\(M_x|\varepsilon|\le\lambda_x/2\)，便得
\[
I-\mathcal U_\varepsilon^*\Phi_\varepsilon\mathcal U_\varepsilon
\succeq \tfrac12\lambda_x\varepsilon^2I.
\]
这证明 (2.6)。

条件 \(m(x)>0\) 只排除了均值零实超平面中的有限多个中央子集和超平面，因而提供稠密的固定方向集合。但**方向稠密不等于存在共同正半径**：方向趋近退化超平面时，上述下界和可用半径可以趋于零。对于 \(B_xf=S_xf=0\) 的源向量，二阶式没有支付高阶项；本稿不把它补成未证明的全邻域结果。

## 8. 可重建的完整层规范核对与后续边界

配套 [精确展开程序](2026-11-14-even-phase-second-variation-original-incidence-789f-next.py) 不使用 (5.5) 的低塔公式，而从完整第一、第二子集包含矩阵的 Gram 及其逆的有理 Taylor 展开独立生成相位系数。它保留非正交原核基的完整度量及物理伴随，并在以下两个固定实例精确核过 (2.2)：

| 位数 | 整个 primitive 源维数 | 均值零方向 | 二阶系数秩 |
|---|---:|---|---:|
| 4 | 3 | \((-6,-2,1,7)\) | 3 |
| 6 | 9 | \((-11,-7,-3,1,8,12)\) | 9 |

这两次完整层校准只核规范和实现，任意 \(s,x\) 的证明是 §§3–7 的算子恒等式。它们没有被用作一般正性的采样证据。

本文得到的是一个新的、全位数的实际正二阶能量，而不是已完成的统一相位界。任意正权的相位预算、退化方向的高阶控制、原 graph 接合及一般 Hilbert 不变子空间问题仍需继续处理。
