# R239 附录：真实高出生块不保持外桥核

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI 辅助：GPT-6 Astra Pro。
状态：已证明原联合旗中 $B_2$、$\mathcal H_2$ 不保持外桥核。尚未对实际更窄的 $\sigma=V_2Q_1^{-1}V_1B_0^{-1}g_0$ 得到能量下界或上界，不据此否定无权目标。

本稿承接 [准确外源与 Vandermonde 正交](R239-appendix-actual-outer-birth-source-factorization-and-vandermonde-orthogonality.md)、
[Vandermonde 原权反例](R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md) 和
[R271 完整链及真实 Schur 补](R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)。
固定原合法 $m\ge5$、$d=2^m$、$4d\le q\le\exp(d^3/4)$。
以下全为原 Hilbert 度量中的等式，没有有限模型替代、carry 近似或未付的头相似变换。

## 1. 结论与准确空间

置
$$
D=\sum_{j\ge m}a_jE_j,\quad C=D_3=\sum_{j\ge m}a_j^3E_j,\quad
D_5=\sum_{j\ge m}a_j^5E_j,\qquad a_j=(j+1)^{-2},
$$
并保留旧记号
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\quad
U_{h,p}=E_{h,p}\ominus E_{h-1,p},\quad K_p=E_{1,p}.
$$
固定层有界双射 $D^{h-1}:U_{h,p}\to K_{p-h+1}$ 的逆为 $\mathfrak J_{h,p}$。

令 $A=A_m$ 为两个原边界之一的真实有限头。采用准确联合旗
$$
\mathscr C_t=\bigoplus_{i=0}^{d-t} e_iE_{d-i,q+t},\qquad
\mathscr Y_t=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t},
$$
$$
(Sc)_t=Ac_t+Dc_{t+1},\qquad \mathcal G=SS^*.
$$
链段 $t=1,\ldots,d$，输出段 $t=1,\ldots,d-1$。
正交高度 $U_{h,p}$ 的出生编号为 $p-h+1$。令
$\mathscr Y_2$ 为出生编号 $\ge q+2$ 的高块，$B_2=P_2\mathcal G|_{\mathscr Y_2}$。
保留原三块消元的外桥 $V_2$、中间 Schur 补 $Q_1$ 及
$$
\mathcal H_2=B_2-V_2Q_1^{-1}V_2^*.
$$
固定 $m,q$ 下这些逆的存在性由旧联合旗有界右逆给出；这里没有声称其范数对 $q$ 一致。

**定理 1.1。** 存在明确的 $b\in\mathscr Y_2$，使
$$
V_2^*b=0,\qquad V_2^*B_2b=0,\qquad V_2^*B_2^2b\ne0.
\tag{1.1}
$$
因此 $\ker V_2^*$ 不被 $B_2$ 保持，也不被 $\mathcal H_2$ 保持。进一步，
$$
\boxed{P_{\ker V_2^*}\mathcal H_2^{-1}V_2\ne0.}
\tag{1.2}
$$
式 (1.2) 只说某些外桥像中的源经过真实 Schur 逆后会进入外桥核。
它没有说这个源可取为由真正 $w\in M\ominus N$ 所产生的更窄实际源。

## 2. 同一个 Vandermonde 向量还满足什么

取 $p=q+3$，令 $I=[m,m+2p)$，将其内部编号为 $0,\ldots,2p-1$。
记 $\alpha_i=a_{m+i}$、$z_i=\alpha_i^2$，这些正数两两不同。
采用原 Vandermonde 构造
$$
X=\sum_{|R|=p}\alpha_R y_R e_R,\qquad
y_R=\frac{\Delta_I}
{\prod_{i\in R,\ j\notin R}(z_j-z_i)},\qquad
\Delta_I=\prod_{i<j}(z_j-z_i).
\tag{2.1}
$$
这里 $\alpha_R=\prod_{i\in R}\alpha_i$；$X$ 未归一化，但非零。
在 $I$ 外张量真空，仍记为 $X$。旧证明给
$$
D_I^*X=0,\qquad D^2X=0,\qquad CDX=0.
\tag{2.2}
$$
令
$$
Y=DX,\qquad F_5=D_5Y.
$$
则 $Y\in K_{p-1}$、$CY=0$，而 $F_5\in K_{p-2}$。

本稿需要的严格非零量是
$$
\boxed{F_5\ne0,\qquad C^2X=-2F_5.}
\tag{2.3}
$$

### 2.1 逐系数证明 $F_5\ne0$

固定 $T\subset I$、$|T|=p-2$，令 $U=I\setminus T$，
$$
P_T(z)=\prod_{t\in T}(z-z_t),\quad
P_U(z)=\prod_{u\in U}(z-z_u),\quad
C_{TU}=\prod_{t\in T,\ u\in U}(z_u-z_t).
$$
旧交叉乘积恒等式为
$$
y_{T\cup\{i,j\}}
=-\frac{\Delta_I}{C_{TU}}\,
\frac{P_T(z_i)P_T(z_j)(z_i-z_j)^2}
{P_U'(z_i)P_U'(z_j)}
\qquad(i\ne j\in U).
\tag{2.4}
$$
置
$$
\beta_i=\frac{z_iP_T(z_i)}{P_U'(z_i)},\qquad
M_\nu=\sum_{i\in U}\beta_i z_i^\nu.
$$
因 $|U|=p+2$，Lagrange 首项系数公式准确给
$$
M_0=M_1=0,\qquad M_2=1.
\tag{2.5}
$$
这里相应分子次数依次为 $p-1,p,p+1$，最后一个为首一。

顺序算子 $D_5D$ 的两个不同删除位给权
$\alpha_i^5\alpha_j+\alpha_j^5\alpha_i$。
代入 (2.4) 后，
$$
(F_5)_T
=-\frac{\alpha_T\Delta_I}{C_{TU}}
\sum_{i<j\in U}\beta_i\beta_j
(z_i-z_j)^2(z_i^2+z_j^2).
$$
准确对称和为
$$
\sum_{i<j}\beta_i\beta_j(z_i-z_j)^2(z_i^2+z_j^2)
=M_0M_4-2M_1M_3+M_2^2=1.
$$
因此
$$
\boxed{(F_5)_T=-\alpha_T\Delta_I/C_{TU}\ne0.}
\tag{2.6}
$$
所有分母均非零。这证明了 (2.3) 的非零部分，不依赖数值秩或一般位置断言。

同样，$C^2$ 的顺序删除给额外因子 $2z_iz_j$，所以
$$
(C^2X)_T
=-\frac{2\alpha_T\Delta_I}{C_{TU}}
(M_1M_3-M_2^2)
=2\alpha_T\Delta_I/C_{TU}.
$$
这也逐系数核对了 $C^2X=-2F_5$，保留了顺序删除的因子 $2$。

### 2.2 后续所需的尾恒等式

令
$$
H_D=[D,D^*]=S_mI-2\sum_{j\ge m}a_j^2n_j,\qquad
F=DD^*,\qquad
s=S_{m+2p}=\sum_{j\ge m+2p}a_j^2>0.
$$
避免把 $H_D$ 与 $C=D_3$ 混同。逐位有
$$
[D,H_D]=-2C,\qquad [C,H_D]=-2D_5.
\tag{2.7}
$$
有限块上 $D_I^*X=0$、$D_I^2X=0$ 给
$$
CX=H_{D,I}Y,\qquad C^2X=-2D_5Y,
$$
与上面的系数计算相符。全尾创建仅来自远尾，故
$$
FX=Y\otimes D_{I^c}^*\Omega+sX.
\tag{2.8}
$$
因此
$$
DFX=2sY,\qquad CDFX=0,\qquad FY=H_DY,\qquad CFY=-2F_5.
\tag{2.9}
$$
此外
$$
\boxed{CDF^2X=-4sF_5.}
\tag{2.10}
$$
具体地，$f=FX\in E_{2,p}$。由
$D^2D^*f=2H_DDf-2Cf$ 得
$$
CDF^2X=2CH_DDFX-2C^2FX.
$$
(2.9) 使第一项为 $-8sF_5$。
(2.8)、$CY=0$ 及远尾一孔向量被 $C^2$ 杀掉，给
$C^2FX=sC^2X=-2sF_5$，所以第二项为 $4sF_5$，即 (2.10)。

下面还使用
$$
D^*Y\in E_{2,p},\qquad D^*X\in E_{3,p+1},\qquad
D^*FX\in E_{3,p+1},\qquad F^2X\in E_{2,p}.
\tag{2.11}
$$
前三式分别由 $CY=0$、$CDX=0$、$CDFX=0$ 和
$D^{h+1}D^*f=-h(h+1)CD^{h-1}f$ 得到。
最后一式可从
$DF^2X=4sH_DY-2CFX$ 再作用 $D$ 得到。
这些核阶确保后面的所有链旗投影确实透明，而不是被省略。

## 3. 第一轮 Gram：保留头部投影

记头前缀正交投影为 $P_{\le r}$，置
$$
a=P_{\le d-3}A^*e_0,\qquad
u=P_{\le d-2}A^*a,\qquad
a_2=P_{\le d-3}A^*Aa.
\tag{3.1}
$$
真实头严格降低编号，$Ae_0=0$，且两个模型都有 $A_{0,1}=1$。
因此 $a\ne0$，其 $e_1$ 分量为 $1$。注意三个投影都保留；没有将 $A^*a$ 或 $A^*Aa$ 换成无投影量。

令 $b$ 只有第 $3$ 输出段非零：
$$
b_3=e_0X.
\tag{3.2}
$$
因为 $X\in E_{2,p}$，其出生编号为 $q+2$ 或 $q+3$，
故 $b\in\mathscr Y_2$。由 (2.11) 和头旗，
$$
(S^*b)_3=aX,\qquad (S^*b)_4=e_0D^*X.
$$
这里第 $3$ 链段保留头至 $d-3$；所有保留头的尾核容量至少为 $3$，
所以 $X\in E_2$ 不再被尾投影削去。
第 $4$ 段头为 $e_0$，容纳 $D^*X\in E_3$。

再作用 $S$，
$$
(\mathcal G b)_2=aY,\qquad
(\mathcal G b)_3=AaX+e_0FX,
\tag{3.3}
$$
其余输出为零，特别第 $4$ 段由 $Ae_0=0$ 消失。
第 $2$ 段在 $E_1$、第 $3$ 段在 $E_2$，所以它们全部属于高出生块。
因此
$$
B_2b=\mathcal G b.
\tag{3.4}
$$

## 4. 第二轮 Gram：全部输出仍在高块

对 (3.3) 再取 $S^*$，准确有
$$
\begin{aligned}
(S^*\mathcal G b)_2&=uY,\\
(S^*\mathcal G b)_3&=a_2X+a(FX+D^*Y),\\
(S^*\mathcal G b)_4&=AaD^*X+e_0D^*FX.
\end{aligned}
\tag{4.1}
$$
其余段为零。第 $2$ 段的头至 $d-2$、尾在 $E_1$；
第 $3$ 段的头至 $d-3$、尾在 $E_2$；
第 $4$ 段的 $Aa$ 头至 $d-4$、尾在 $E_3$。
这些范围均在原 $\mathscr C_t$ 内，因而 (4.1) 已包含全部头及尾投影。

记 $v=\mathcal G^2b$。第 $1$ 段为 $DuY=0$；其余非零段是
$$
\begin{aligned}
v_2&=(Au+a_2)Y+a(DFX+FY),\\
v_3&=Aa_2X+Aa(2FX+D^*Y)+e_0F^2X,\\
v_4&=A^2aD^*X.
\end{aligned}
\tag{4.2}
$$
它们依次在 $E_1,E_2,E_3$，故出生编号全部 $\ge q+2$。
头范围分别至 $d-3,d-4,d-5$，也都合法。
所以
$$
\boxed{B_2^2b=\mathcal G^2b=v.}
\tag{4.3}
$$
这一步没有忽略高块压缩。

由 (2.9)--(2.10) 得到外桥需要的最高删除坐标：
$$
\boxed{
Cv_2=-2aF_5,\qquad
CDv_3=-2AaF_5-4s e_0F_5,\qquad
CD^2v_4=0.
}
\tag{4.4}
$$
最后一式使用 $D^2D^*X=2sY$ 与 $CY=0$。

## 5. 外桥检测到严格非零项

保留出生层分解 $S=S_0+S_1$；$S_0$ 保持出生编号，
$S_1$ 增加出生编号一。外桥准确为
$$
V_2=S_1S_0^*,\qquad V_2^*=S_0S_1^*
$$
在出生编号 $q+1$ 与 $q+2$ 的相应限制。

对第 $t$ 段出生编号 $q+2$ 的尾高度 $U_{t-1,q+t}$，
旧准确两带式为
$$
(S_1^*f)_{t+1}
=-t(t-1)\mathfrak J_{t+1,q+t+1}CD^{t-2}f_t.
\tag{5.1}
$$
若 $f_t\in E_{t-1,q+t}$，先投到最高高度也不改变右端，
因为 $D^{t-2}$ 杀掉 $E_{t-2,q+t}$。因此 (5.1) 可直接用于 (3.2)、(3.3)、(4.2) 的对应段。
高于 $q+2$ 的出生编号不参与这个外桥限制。

由 $CDX=0$、$CY=0$ 和 $CDFX=0$，
$$
V_2^*b=0,\qquad V_2^*B_2b=0.
\tag{5.2}
$$
对 $v=B_2^2b$ 用 (4.4)，$S_1^*v$ 在出生编号 $q+1$ 的非零链段为
$$
\begin{aligned}
(S_1^*v)_3&=4a\,\mathfrak J_{3,q+3}F_5,\\
(S_1^*v)_4&=12(Aa+2s e_0)\,\mathfrak J_{4,q+4}F_5.
\end{aligned}
\tag{5.3}
$$
其余对应段为零。头范围允许这些高度，不需再删去分量。

将 $S_0$ 作用到 (5.3)，第 $2$ 输出段只有第 $3$ 链段的第一下降贡献。
固定层第一下降的准确相容式给
$$
D^{(0)}\mathfrak J_{3,q+3}=\mathfrak J_{2,q+2}.
$$
所以
$$
\boxed{
(V_2^*B_2^2b)_2
=4a\,\mathfrak J_{2,q+2}F_5\ne0.
}
\tag{5.4}
$$
这里 $F_5\in K_{q+1}$、$F_5\ne0$，
$\mathfrak J_{2,q+2}$ 单射，$a\ne0$；
第 $2$ 输出头至 $d-3$，尾高度为 $2$，完全在原中间块中。
这证明 (1.1)。

## 6. Schur 逆的混合及其严格量词

取 $b'=B_2b$。由 (5.2)，$b'\in\ker V_2^*$；
但 (5.4) 说明 $B_2b'\notin\ker V_2^*$。
因此普通高块确实不保持这个核。
在该核上
$$
\mathcal H_2b'=B_2b',
$$
所以 $\mathcal H_2$ 也不保持它。

再令 $\mathscr R=\overline{\operatorname{Ran}V_2}=(\ker V_2^*)^\perp$。
若 (1.2) 不成立，连续性使有界自伴算子
$\mathcal H_2^{-1}$ 保持 $\mathscr R$。
自伴性继而使其保持 $\mathscr R^\perp$，即这两个空间减少
$\mathcal H_2^{-1}$。因为 $\mathcal H_2$ 有界可逆，
它也与这两个正交投影交换，矛盾。
这证明 (1.2)，不需要假设 $\operatorname{Ran}V_2$ 闭。

这个例子精确落实了旧外源稿中的警戒：
源正交
$\sigma\perp\ker V_2^*$
不能直接传成
$z_2=\mathcal H_2^{-1}\sigma\perp\ker V_2^*$。
原来的合法结论仍是
$$
\langle z_2,B_2b\rangle=0\qquad(b\in\ker V_2^*).
$$

然而，(1.2) 只涉及全部外桥像。
实际源还具有
$$
\sigma=V_2Q_1^{-1}V_1B_0^{-1}g_0,\qquad
g_0=S b_y,\quad b_y=P_{\mathscr C}D_0^*y,
$$
以及真正 $w\in M\ominus N$ 的残量约束。
本稿没有证明所构造的混合源来自这一更窄集合，
没有给 $\langle\mathcal H_2^{-1}\sigma,\sigma\rangle$ 的增长，
也没有否定真实源仍可能具有额外取消。
后续仍需在实际 Schur 度量中支付这个准确源，或控制
$\widetilde C_{\rm tot}(h(z))$ 的真正合成范数。
