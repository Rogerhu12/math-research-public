# R239 附录：四块天然零源旗与同一首 primitive 的裸链运输

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：模型天然零源旗的全部原廉价右链、同源 Schur、真正模型左最小化，以及无需比较裸投影的可行低链运输均已证明。裸链运输入口由根代理提出，本稿核全高出生补全、primitive 参数化和孔域。原自然模型的平坦费用运输尚不作为本稿已证输入；普通 ISP 与 $N=M$ 均为 OPEN。

沿用[原四块头比较、四分之一深度消元与全部自由头反馈](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)，固定
$m\ge8,d=2^m,p=d/4,4d\le q\le e^{d^3/4}$，
原 $A=A_m,D=D_m$ 和实际比较头
$$
A_\square=I_4\otimes A_{m-2}
 +(b_{m-2}E_0+b_{m-1}E_1)\otimes I_p.
$$
前稿证明完整 primitive 延拓差
$$
\|\mathcal E_A^{\rm full}-\mathcal E_\square^{\rm full}\|
\le\varepsilon=e^{-d^4/20}.
\tag{0.1}
$$
所有内容在同一尾 $D_m$、同一物理 $d$ 头及同一 $q$ 中读取。

## 1. 天然模型零源旗准确包含原自由旗

对任意严格降头的有限幂零头 $T$，记
$$
\mathcal E_T^{\rm full}a=\sum_{k=0}^{d-1}(-T)^kQ_ka,\quad
\mathcal E_T=P_{\le q}\mathcal E_T^{\rm full},\quad
\mathcal B_Ta=T(\mathcal E_Ta)_q.
$$
在原 primitive 空间
$\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^qK_n$ 上，
$$
\mathcal B_Ta
=\sum_{t=0}^{d-2}(-1)^tQ_tT^{t+1}a_{q-t}.
\tag{1.1}
$$
尾顺次 Taylor 展开唯一，所以
$$
\boxed{
\ker\mathcal B_T
=\bigoplus_{n=0}^q
\bigl(\ker T^{q-n+1}\otimes K_n\bigr).
}
\tag{1.2}
$$
如果 $a$ 属于 (1.2)，每个输入 $a_{q-t}$ 的所有 $T^ka_{q-t}$、$k\ge t+1$ 都为零。因此
$$
\boxed{P_{>q}\mathcal E_T^{\rm full}a=0.}
\tag{1.3}
$$
这比只说第 $q$ 层源为零更明确地支付了整段右支撑。

原 $A_m$ 的首上对角线非零，故
$\ker A_m^{t+1}=H_{\le t}$（当 $t\ge d-1$ 时为全部头）。
$A_\square$ 也严格降物理头，所以
$H_{\le t}\subseteq\ker A_\square^{t+1}$。因此
$$
\boxed{
\mathscr F:=\ker\mathcal B_A
\subseteq\mathscr F_\square:=\ker\mathcal B_\square.
}
\tag{1.4}
$$
定义真正物理正交分解
$$
\mathscr Y=\mathscr F_\square\ominus\mathscr F,\qquad
\mathscr T_\square=\mathscr F_\square^\perp.
$$
原强制空间 $\mathscr T=\mathscr F^\perp$ 于是满足
$$
\boxed{\mathscr T=\mathscr T_\square\oplus\mathscr Y.}
\tag{1.5}
$$
$\mathscr Y$ 是原强制源坐标中的闭空间；它并未被假定与首源头坐标 $\Delta$ 正交。

由于 $A_\square^{p+2}=0$，$\mathscr T_\square$ 只含 $0\le t\le p$，更准确地
$$
\boxed{
\mathscr T_\square
=\bigoplus_{t=0}^{p}
(\ker A_\square^{t+1})^\perp\otimes K_{q-t}.
}
\tag{1.6}
$$
这同时保留浅层内模型新增的所有核方向，而不只消去深 jets。

## 2. 全部新增零源方向都有原廉价右旗

对 $a\in\mathscr Y\subset\mathscr F_\square$，(1.3)、(0.1) 给
$$
R_Ya=-P_{>q}\mathcal E_A^{\rm full}a
=-P_{>q}(\mathcal E_A^{\rm full}-\mathcal E_\square^{\rm full})a,
\qquad \|R_Ya\|\le\varepsilon\|a\|.
$$
前稿逐项核过的原完整右旗适用于任意 primitive 输入：第 $k$ 次原尾提升的尾核阶为至多 $k+1$，头至多 $d-1-k$，所以全部联合旗合法。左右源切分给
$$
\boxed{
R_Y:\mathscr Y\to\ker S_{\rm flag},\qquad
F_{\rm flag}R_Ya=B_Ua,\qquad
\|R_Y\|\le\varepsilon.
}
\tag{2.1}
$$
它是原 $A_m$ 的真正可行链，源坐标纯粹为 $a$，没有低锚。

单独在源子空间 $B_U\mathscr Y$ 上，还可直接得
$$
\mu(r)^2\le\lambda(r)\lambda_{\rm flat}(r)
\le\varepsilon\mu(r)\lambda_{\rm flat}(r),
$$
故
$$
\boxed{\mu(r)\le\varepsilon\lambda_{\rm flat}(r)
\qquad(r\in B_U\mathscr Y).}
\tag{2.2}
$$
因此该子空间自身的 $M$ 投影费用为 $\varepsilon^2$。本稿没有据此声称它与整个首源头的和也有相同常数；两者的角度未被免费处理。

## 3. 同一平坦源下的天然旗 Schur

把原完整源 Schur $S=\mathcal G_q\succeq I$ 按
$\mathscr T_\square\oplus\mathscr Y$ 分块。对原源 $r$ 写
$\Gamma_qr=(x,y)$，置
$$
y_0=-S_{11}^{-1}S_{10}x,\quad z=y-y_0,\quad
\widehat S=S_{00}-S_{01}S_{11}^{-1}S_{10}\succeq I.
$$
(2.1) 与原同一个 $c^\flat=F_{\rm flag}^*J_q^{-1}r$ 给
$$
S_{11}z=R_Y^*c^\flat.
$$
令
$$
r_{\rm cut}=B_U(x,y_0),\qquad\delta r=B_U(0,z).
$$
则
$$
\boxed{
\mu(r)^2=\mu(r_{\rm cut})^2+\mu(\delta r)^2,\qquad
\mu(\delta r)\le\varepsilon\lambda_{\rm flat}(r),
}
\tag{3.1}
$$
$$
\boxed{
\lambda(\delta r),\alpha(\delta r)
\le\varepsilon^2\lambda_{\rm flat}(r).
}
\tag{3.2}
$$
真正裸最小链相应只改变至多 (3.2)。

取原完整右浅列 $R_X$，剩余双配对保持为
$$
\boxed{
\widehat Sx=\widehat R^*c^\flat(r),\qquad
\widehat R=R_X-R_YS_{11}^{-1}S_{10}.
}
\tag{3.3}
$$
$y_0$ 可以非零；没有把模型额外零源方向变成原来源的支撑空白。

## 4. 现在模型最小化的约束确实是天然源约束

原全部自由坐标连同 (3.1) 中最小化的 $\mathscr Y$，准确合成
$\mathscr F_\square$。因此
$$
p_A=x+f_A,\qquad
f_A\in\mathscr F_\square,\qquad
v_A=\mathcal E_Ap_A=E_q^\dagger r_{\rm cut}
$$
是在同一个仿射空间 $x+\mathscr F_\square$ 内的真正最小者。

在同一仿射空间内最小化 $\|\mathcal E_\square p\|$，记为
$p_\square=x+f_\square$、$v_\square=\mathcal E_\square p_\square$。
由 (1.2)，这个仿射空间恰是比较头固定源
$$
\boxed{g=\mathcal B_\square x}
\tag{4.1}
$$
的所有 primitive 参数，所以 $v_\square$ 确为模型自己的天然左最小前驱。

固定参数下这一源空间是闭的：其元素可用尾 Taylor jets 描述为
$P_0D^tr\in\operatorname{Ran}A_\square^{t+1}$、$0\le t\le p$，
以及 $D^{p+1}r=0$。每个头范围有限维闭，Taylor 正反变换及
$A_\square^{t+1}|_{(\ker A_\square^{t+1})^\perp}$ 的逆在固定参数下有界。
故天然最小逆确实存在；本段没有给其范数免费的统一上界。

应用前稿根代理给出的双正规方程比较，得到
$$
\boxed{
(1+\varepsilon)^{-1}\mu_A
\le\mu_\square\le(1+\varepsilon)\mu_A,
}
\tag{4.2}
$$
$$
\boxed{
\|v_A-v_\square\|\le3\varepsilon(1+\varepsilon)\mu_A,
\qquad
\|p_A-p_\square\|\le2\varepsilon(1+\varepsilon)\mu_A.
}
\tag{4.3}
$$
其中 $\mu_A=\mu(r_{\rm cut})$、$\mu_\square=\|v_\square\|$。
这次 (4.1) 已合法识别为模型天然源，而不是把上一稿较小的自由旗直接换名。

## 5. 任意严格降头的裸低链都可补成完整链

本节对任意严格降物理头的 $d\times d$ 矩阵 $T$ 成立，包括退化的 $A_\square$；不要求首上对角线非零。

沿原宽度 $d$ 的联合输入旗，第 $t$ 段在孔层 $q+t$，头 $i\le d-t$，尾属于 $E_{d-i,q+t}$。低出生投影在第 $t$ 段保留尾高度至少 $t$，即
$$
P_{L,t}=I-P_{E_{t-1,q+t}}.
$$
设 $a=(a_1,\ldots,a_d)$ 是一个可行裸低链：首输出 $Da_1=r$，每个内部输出
$Ta_t+Da_{t+1}$ 的低出生投影为零。

逐行构造高出生补全 $h_t$。取 $h_1=0$。在第 $t<d$ 行，已知 $h_t$ 后，剩余高输出
$$
b_t=Ta_t+Da_{t+1}+Th_t
$$
属于 $E_{t-1,q+t}$；其头指标至多为 $d-t-1$，因为 $T$ 严格降头，而下一段本来只允许这些头。定义
$$
h_{t+1}=-D_{q+t+1}^\dagger b_t.
\tag{5.1}
$$
固定层原 $D^\dagger$ 有界，且
$D^{t-1}b_t=0$ 与 $Dh_{t+1}=-b_t$ 直接给
$h_{t+1}\in E_{t,q+t+1}$。因此它是第 $t+1$ 段的高出生部分，并仍满足所有头/尾联合旗。
式 (5.1) 使该行准确归零。最后一段只有头零，所以 $T(a_d+h_d)=0$ 自动成立。

因此
$$
\boxed{c=a+h\in\ker S_{\rm flag,T},\qquad
F_{\rm flag,T}c=r,\qquad P_Lc=a.}
\tag{5.2}
$$
本证明不需模型高出生 Schur 的额外满射假设；完整 Taylor 递推已支付补全。补全的范数可以很大，本节只用其存在性，不将它当成裸最小链。

## 6. 裸链的唯一有效自由参数是右首 primitive

给定一个原左 primitive 参数 $p_0$，其源是 $r=\mathcal B_Tp_0$。
规范完整右链为
$$
c^{\,r}=-P_{>q}\mathcal E_T^{\rm full}p_0.
$$
它的第一段 primitive 投影为零，因为每个右输出都包含正次 $Q_k$。

任一其它完整同源链与 $c^{\,r}$ 的差是右侧零首源完整核。按右孔层的 primitive 参数 $h_j$、$1\le j\le d$ 展开，它准确为
$$
\sum_{j=1}^d Z_{T,j}^+h_j,\qquad
Z_{T,j}^+h_j
=\sum_{k\ge0}(-T)^kQ_kh_j,
\tag{6.1}
$$
其中 $h_j$ 位于第 $q+j$ 孔层、头不超过 $d-j$。
严格降头保证该和在第 $d$ 段前终止，且全旗合法。

来自 $h_j$ 的第 $k$ 次提升在段 $t=j+k$，尾核阶至多 $k+1$，故其出生至少为
$t-(k+1)+1=j$。所以
$$
\boxed{P_LZ_{T,j}^+h_j=0\quad(j\ge2).}
\tag{6.2}
$$
只有 $h=h_1\in\mathbb C^d\otimes K_{q+1}$ 可改变裸低链。结合 §5 的任意裸链可补全性，
$$
\boxed{
\alpha_T(r)
=\min_{h\in\mathbb C^d\otimes K_{q+1}}
\left\|P_L\left[-C_Tp_0+Z_T^+h\right]\right\|,
\quad C_T=P_{>q}\mathcal E_T^{\rm full},
\quad Z_T^+=Z_{T,1}^+.
}
\tag{6.3}
$$
其最优参数准确为真正裸链第一段的 primitive 部分：
$$
\boxed{h=P_0a_1(r),\qquad\|h\|\le\alpha_T(r).}
\tag{6.4}
$$
因为第一段属于低出生，规范链的 primitive 为零，所有其它右 primitive 对该段无贡献。映射 $h\mapsto P_LZ_T^+h$ 的范数下界为一，故最小化的像闭、极小值确实取得。

## 7. 同一个 p_A 与 h 的模型裸费用运输

在 (6.3) 取原实际 $T=A_m$、$p_0=p_A$，令 $h$ 为它的真正最优参数。把同一个 $p_A,h$ 用到 $T=A_\square$。

由于 $p_A-x\in\mathscr F_\square$，(1.3) 给
$$
C_\square p_A=C_\square x.
\tag{7.1}
$$
所以所得模型完整右链的源正是天然模型源 $g$。

(0.1) 控制 $C_A-C_\square$。右首 primitive 在 $q+1$，所需共同常数变成
$$
\mathcal L_+
=512\sqrt{q+2d}(m+q+2d)^{3/2}<2048q^2.
$$
因为 $q\ge4d$、$m\le d$，两因子分别不超过
$(3q/2)^{1/2}$ 和 $(7q/4)^{3/2}$，故同一四次账本仍给
$$
\|Z_A^+-Z_\square^+\|\le\varepsilon.
\tag{7.2}
$$
没有把 $q+1$ 直接当成满足原上窗的新 $q$；这里是用原同一个 $q$ 重核完整常数。

$P_L$ 是同一物理出生投影，故模型候选的费用给
$$
\begin{aligned}
\alpha_\square(g)
&\le\alpha_A(r_{\rm cut})
+\varepsilon\|p_A\|+\varepsilon\|h\|\\
&\le
\boxed{(1+\varepsilon)\alpha_A(r_{\rm cut})
+\varepsilon\mu_A(r_{\rm cut}).}
\end{aligned}
\tag{7.3}
$$
这里没有比较两个不稳定的裸最小投影，只运输一个明确可行的低链。

再代入 (3.2)，得到完全保原源的版本
$$
\boxed{
\alpha_\square(g)
\le(1+\varepsilon)\alpha_A(r)
+\varepsilon\mu_A(r)
+(1+\varepsilon)\varepsilon^2\lambda_{{\rm flat},A}(r).
}
\tag{7.4}
$$

## 8. 已闭范围与仍待支付的平坦源

以上保留了同一原 $r$ 的：

- 左 Schur 小偏离 (3.1)；
- 原平坦向量在剩余方程 (3.3) 中不变；
- 天然模型源 $g=\mathcal B_\square x$ 的真实最小左前驱及 (4.2)–(4.3)；
- 同一个实际 $p_A$ 与首 primitive $h$ 的模型裸费上界 (7.4)。

尚未在本稿中从这些结论推出
$\lambda_{{\rm flat},\square}(g)$ 的相应上界。
左右最小能量的二次形接近不自动运输非交换的平坦变换；普通源差也不支付裸或平坦逆。后续应在同一自然模型源空间中构造真正对偶测试及其头条件数账本，不能把 (7.4) 当成已经完成三种费用的全部运输。
