# 原 unit211 的紧凑均值与 N1：不用统一 Gram 分母的四条标量二次式

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 原定义与范围

本稿是原 unit211 方程的完整多项式恒等式，不预设 $\Phi=0$。它提供后续同一点局部化计算可直接采用的四条二次式。没有排空某个权面，也没有构造新不变子空间。

令
$$
\ell=b+c,\quad a=1-\ell,\quad \delta=b-c,\quad
p=1+\rho,\quad q=1-\rho,\quad Q=1-\rho^2,
$$
$$
u=bp+cq,\quad V_2=bp^2+cq^2,\quad T_0=V_2-2u^2.
$$
为避免同名混淆，本稿 $\delta=b-c$，并非部分旧稿中的 $1-Q$。

在原四维代数中，乘法和迹为
$$
(vw)_0=v_0w_0,\quad
(vw)_1=v_0w_1+v_1w_0,\quad
(vw)_2=v_2w_2,\quad(vw)_3=v_3w_3,
$$
$$
\tau(v)=av_0+v_1+bv_2+cv_3.
$$
单位为 $\mathbf1=(1,0,1,1)$。取自由原变量 $f,X,Y,t$，令
$$
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A=2f-2bX-2cY+2bc\,t
$$
及对称原 Gram
$$
\mathcal G=
\begin{pmatrix}
0&0&p&q\\
0&A&r&s\\
p&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$
记其第 $j$ 行为 $g_j$，算子 $(Kv)_j=\tau(g_jv)$，
$d=K\mathbf1$，$F_2=\tau(d)=2f$。原均值按
$$
E_j=\tau(g_j^2)-2(Kd)_j-2d_j^2+2F_2d_j
\quad(j=0,B,C)
$$
定义，而
$$
E_1=2\tau(g_0g_1)-2(Kd)_1-2d_1^2+2F_2d_1.
$$
这是已有原输入使用的归一，$E_1$ 没有另加一半。

令
$$
V=bX+cY,\qquad U=bX-cY,\qquad
W=bpX+cqY=V+\rho U.
$$
则原
$$
E_0=T_0-2W+4uf.
$$

## 2. 紧凑变量及两条均值组合

在原 $E_0=0$ 上定义
$$
z=Qt,\qquad V_n=QV,\qquad
W_*=T_0+4uf=2W,\qquad
N=QW_*-2V_n=2Q\rho U.
$$
下述所有式关于 $f,z,V_n,W_*,N$ 至多二次。后续用原 E0/N0 恢复 $V_n$ 后，它们就是关于 $f,z$ 的标量二次式；不必重新组装含统一几何分母的整 Gram。

记
$$
I=(V_n+auQ)^2-2uQV_n+2au^2Q^2-4aufQ^2
   +bc\,z^2+z(4bc\,uQ-\ell V_n),
$$
$$
R_2=2\rho I+\delta zN.
$$
设 $E_W=bE_B+cE_C$，则
$$
R_2=-\rho Q^2(E_1-E_W)\qquad(E_0=0).
$$

另一条为
$$
\begin{aligned}
W_4={}&8bc\,\rho^2Q^2\ell T_0
 -4\ell\rho^2V_n^2-\ell N^2+4\delta\rho V_nN\\
&+32bc\,\rho^2QfV_n+16b^2c^2\rho^2z^2\\
&+32b^2c^2\rho^2Q(u-1)z
 -8bc\,\ell\rho^2zV_n+4bc\,\delta\rho zN.
\end{aligned}
$$
它满足
$$
W_4=8bc\,\rho^2Q^2E_W\qquad(E_0=0).
$$

这两式有完整原多项式来源。即使不先设 $E_0=0$，仍取
$N=QT_0+4Quf-2QV$，则精确恒等式为
$$
R_2+\rho Q^2(E_1-E_W)-Q^2(\delta t-a\rho)E_0=0,
$$
$$
W_4-8bc\,\rho^2Q^2E_W
 -4Q^2E_0\bigl(2bc\,\rho^2+bc\,\rho\delta t
              -\rho(\ell U-\delta V)\bigr)
 +\ell Q^2E_0^2=0.
$$
因此这里不是只在某个数值样本相合。

## 3. 个别 B/C 均值的差

再设
$$
S_*=2\rho\ell V_n-\delta N,\qquad
D_*=-2\rho\delta V_n+\ell N.
$$
在 $E_0=0$ 上，
$$
S_*=4bc\,Q\rho(X+Y),\qquad
D_*=4bc\,Q\rho(X-Y).
$$
定义
$$
\begin{aligned}
O_8={}&32b^2c^2aQ^2\rho^3(u-1)
 +4bc\,Q\rho^2S_*+32b^2c^2Q\rho^3V_n
 -64b^2c^2Q^2\rho^3f\\
&+4bc\,Q\rho(1-u+2f)D_*-S_*D_*\\
&-8b^2c^2\rho^2\delta z^2
 -16b^2c^2Q\rho^2z\bigl(\delta(u-1)+\ell\rho\bigr)
 +8b^2c^2\rho zN.
\end{aligned}
$$
其确切原来源是
$$
O_8=8b^2c^2Q^2\rho^2(E_B-E_C).
$$
若把 $W_*$ 取为实际 $2W$、$N$ 取为实际 $2Q(W-V)$，本式甚至是不要求 $E_0=0$ 的完整自由变量恒等式。

在原 $bcQ\rho\ell\ne0$ 域上，$R_2=W_4=O_8=0$ 与
$E_1=E_B=E_C=0$ 等价，前提只保原 $E_0=0$。确实，前两式给 $E_1=E_W=0$，第三式给 $E_B=E_C$，再由 $E_W=\ell E_C$ 收尾。这里用的 $\ell$ 是原已付单位，没有引入范数或首项逆。

## 4. 原 N1 的极化项

定义原 $N_4$ 的极化项
$$
\begin{aligned}
N_v={}&4\tau(dg_0g_1)-2F_2\tau(g_0g_1)\\
&-4\{\tau(g_0)\tau(dg_1)+\tau(g_1)\tau(dg_0)\}
 +4F_2\tau(g_0)\tau(g_1)\\
&+\tau(g_0Kg_1)+\tau(g_1Kg_0).
\end{aligned}
$$
令
$$
\alpha=\ell(1-u)-\rho\delta,\quad
\beta=\rho\ell-\delta(1-u),
$$
$$
A_V=(2u-1)\ell+3\rho\delta,\qquad
B_U=(2u-1)\delta+3\rho\ell.
$$
以下十三项式保留这个实际原 $N_v$：
$$
\begin{aligned}
N_*={}&\alpha(4\rho^2V_n^2+N^2)+4\beta\rho V_nN\\
&+8bc\,\rho^2QV_nW_*
 -24bc\,\rho^2Q^2fW_*\\
&+16abc\,\rho^2Q^2(u-1)W_*
 +64bc\,\rho^2Q^2uf^2\\
&-32bc\,\rho^2QufV_n
 +16bc\,\rho^2Q^2(1+a)T_0f\\
&+16bc\,\rho^2Q(aQ-T_0)V_n\\
&+4bc\,\rho^2A_VzV_n-2bc\,\rho B_UzN\\
&+16b^2c^2\rho^2Qz(2f+T_0-aQ)
 -8ub^2c^2\rho^2z^2.
\end{aligned}
$$
准确恒等式是
$$
N_*=4bc\,\rho^2Q^2N_v.
$$
同样，使用实际 $W_*=2W$、$N=2Q(W-V)$ 时，本式不需要 $\Phi$、$E_0$ 或任何矩方程。

原
$$
N_1=N_v-\frac{4\lambda}{3}P_j.
$$
在已经支付的同一点 P1 来源上 $P_j=3wP_{02}$，故原 N1 只需新增项
$$
N_1^*=N_*-16bc\,\rho^2Q^2\lambda wP_{02}.
$$
此时 $N_1^*=4bc\,\rho^2Q^2N_1$。不能在没有该原 P1 来源的自由 Gram 上把 $N_v$ 自身称为 $N_1$。

## 5. 接入同一点恢复的方式

在原 E0/N0 恢复中，
$$
J=2u(1-u)+\ell Q,\qquad
G=\lambda P_{02}+(u-1)T_0,
$$
并有
$$
V_n=Jf-G+bc\,z,\qquad z=Qt.
$$
所以以上四条式只需原 $f,z$ 及低阶权参数。特别在当前 $\Phi=0$ 图，可用
$$
f=-\frac{P_{c,1}}{P_{f,1}},\qquad
z=\frac{N_{F,2\rho}P_{c,1}-N_{C,2\rho}P_{f,1}}
        {P_{f,1}\,bc\,S\,L_{\mathrm{num}}}.
$$
这里 $P_f=(u-1)P_{f,1}$、$L_{\mathrm{num}}=2\rho\zeta$，分母都由原单位支付。只把 $P_{f,1}$ 与 $L_{\mathrm{num}}$ 作为显名几何分母即可；不需要把它们的商代数范数倒置。

在一个二次 $\rho$ 商中，四条式仍是同一个实际 $\rho$ 的必要零式，不能把每条的两个系数分别置零。合法的新输入是这些实际两列行的完整同点组合或固定行列式。

## 6. 精确执行凭据

源使用七个自由变量
$$
b,c,\rho,f,X,Y,t
$$
的稀疏 BigInt 整数多项式。它从上面原 Gram、原代数乘法、迹、均值和 $N_v$ 定义构造所有式，完成六个完整零差检查：原 $F_2$、原 $E_0$、$R_2$、$W_4$、$N_*$、$O_8$。没有数值代入，没有把原点假设悄悄加入多项式环。

- 源 blob：`94b2be74c729ee76e239491d8e967dc9c41044b0`。
- 源 SHA256：`9ab0270fe53a0a6f169755f92f731e6cf636f1d9b7a9e12364ef487a01cdea6e`；5812 字节。
- 实际执行方式：当前可用 V8 中 `Function(source)()`，并非未执行的 Node 脚本。
- 实际 16 毫秒；624 次整数多项式乘法。
- 自由变量全展开项数：$R_2$ 为 229，$W_4$ 为 486，$N_*$ 为 286，$O_8$ 为 120。
- 完整实际凭据 blob：`a599521d4623cb634a64d09d3f364c623220acd3`。

本稿提供已完成的原代数恒等式及其实际来源。随后首次执行某个参数图的约化时，可以直接引用这些等式，不把再次整 Gram 展开设为前置门槛。
