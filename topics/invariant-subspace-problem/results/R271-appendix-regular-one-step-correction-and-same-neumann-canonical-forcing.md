# R271 附录：同一有限 Neumann 列的正则修正与规范 forcing 身份

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文补[原算子乘积窗口右逆](R271-appendix-true-global-anisotropic-low-head-growing-tail-adjoint-readout.md)的一个同源版本。使用既有 $G_{7\to3}$，可使一次修正后的右逆整个落在 $\mathscr X_3$。因此它与有限规范原像的差落入真实稳定范围。对 $N^\perp$ forcing，得到原有限 Neumann 列 $G_0^*f$ 与规范形式读数之间的超快误差界，而非只知道某个高位平均代表有小范数。

## 1. 同一原列与已付两权右逆

取原 $T_N$ 或 $T_Y$，记
$$
M=\ker T,\qquad \mathcal N=\overline{BM}.
$$
对非负整数 $s,N$，沿原算子窗口稿选
$$
u=N+s+1024,\qquad m=\lceil\log_2u\rceil,\qquad
d=2^m,\qquad x=48u,\qquad R=x-m,\qquad h=d+R.
\tag{1.1}
$$
保持同一物理投影
$$
\Pi=P_{\{\text{前 }x\text{ 位孔数}\le s\}}
P_{\{\text{位 }i\ge x\text{ 孔数}\le N\}}.
$$
令 $C=A_m+D_{[m,x)}$、$\mathcal L_m=C+D_x$，并使用前稿同一逐层远尾逆 $\mathcal Q_x$ 和同一列
$$
G_0=\sum_{k=0}^{h-1}(-C)^k\mathcal Q_x^{k+1}\Pi.
\tag{1.2}
$$
已付
$$
\mathcal L_mG_0=\Pi,\qquad
\|G_0\|\le\mathcal B_s(x),\qquad
\operatorname{Ran}G_0\subseteq\mathcal H_{\le q_0},
\quad q_0=N+s+m+d<4u,
\tag{1.3}
$$
其中
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\tau_x=\log(7\sqrt{2/S_x}),\qquad
\mathcal B_s(x)=(s+3)\sqrt{2/S_x}\,e^{s\tau_x+\tau_x^{4/3}}.
$$
(1.3) 的孔数支撑使用未归并的 $A_m^aD_<^b$，对原 N/Y 两型均成立。

[R239 混合低孔正则提升](R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md) §2 已证明
$$
\|z\|_{\mathscr X_a}=\sum_{q\ge0}e^{aq}\|\mathsf P_qz\|,
$$
$$
G_{7\to3}:\mathscr X_7\longrightarrow\mathscr X_3,\qquad
TG_{7\to3}=I,\qquad
\|G_{7\to3}\|\le C_G=\frac43e^{2^{24}},
\tag{1.4}
$$
以及
$$
M\cap\mathscr X_3\subseteq\mathcal N.
\tag{1.5}
$$
这里只调用已证明的实际输入、输出两权结论；不从 $\mathscr X_3\to\mathcal H$ 的旧右逆自行推断正则输出。

## 2. 同一 carry 残量在 $\mathscr X_7$ 中

原逐位局部片为
$$
T-\mathcal L_m=\sum_{L\ge m}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}},
$$
$$
K_L\mathcal H_{\le q}\subseteq\mathcal H_{\le q+L+1}.
\tag{2.1}
$$
令
$$
E=(T-\mathcal L_m)G_0.
$$
对 $L=m+t$，其第 $t$ 片输出总孔至多 $b=q_0+m+t+1$，故
$$
\|K_{m+t}G_0\|_{\mathcal H\to\mathscr X_7}
\le52\mathcal B_s(x)\sqrt{b+1}\,
e^{7b-770\,16^{m+t-1}}.
\tag{2.2}
$$
与前稿的 $\mathscr X_3$ 估计一样，$b+1\le6u(t+1)$，而现在
$$
\log52+\tfrac12\log(b+1)+7b
\le44u(t+1)\le44u\,16^t.
$$
由 $d\ge u\ge1024$，
$$
770\,16^{m+t-1}\ge48.125u^4\,16^t,\qquad
48.125u^4-44u\ge41u^4.
$$
逐 $t$ 求和得到
$$
\boxed{
\|E\|_{\mathcal H\to\mathscr X_7}
\le e^{-40u^4}\mathcal B_s(x).
}
\tag{2.3}
$$
所以全部 carry 片在真正的 $\mathscr X_7$ 中绝对收敛，且极限就是原差 $(T-\mathcal L_m)G_0$。层数平方根与完整输出权都已计入。

## 3. 正则右逆与精确成本

定义
$$
\boxed{
G_{\rm reg}=G_0-G_{7\to3}E.
}
\tag{3.1}
$$
(1.3) 使 $G_0$ 本身是从窗口 Hilbert 空间到 $\mathscr X_3$ 的有界映射，具体可用
$$
\|G_0\|_{\mathcal H\to\mathscr X_3}
\le\sqrt{q_0+1}\,e^{3q_0}\mathcal B_s(x).
$$
再结合 (1.4)、(2.3)，有
$$
G_{\rm reg}\mathcal H\subseteq\mathscr X_3,
\qquad
TG_{\rm reg}
=TG_0-E=\mathcal L_mG_0=\Pi.
\tag{3.2}
$$
原 Hilbert 范数中的修正量满足
$$
\|G_{\rm reg}-G_0\|
\le C_Ge^{-40u^4}\mathcal B_s(x)
\le e^{-39u^4}\mathcal B_s(x).
\tag{3.3}
$$
最后使用
$$
\log C_G=2^{24}+\log(4/3)<u^4
\quad(u\ge1024).
$$
因此
$$
\boxed{
\|G_{\rm reg}\|
\le(1+e^{-39u^4})\mathcal B_s(x).
}
\tag{3.4}
$$
正则输出的范数可以很大；(3.3)–(3.4) 只估计所需的物理 Hilbert 范数，不把两种范数混同。

## 4. 模稳定范围与同一个规范形式读数

对有限整数支撑 $v\in\Pi\mathcal H$，令 $Jv$ 是 $TJv=v$、$(Jv)_0=0$ 的规范有限三角解。它仍有限整数支撑，故 $Jv\in\mathscr X_3$。由 (3.2)，
$$
G_{\rm reg}v-Jv\in M\cap\mathscr X_3\subseteq\mathcal N.
\tag{4.1}
$$
这一次使用的是已付正则核判据 (1.5)，不要求 $G_{\rm reg}$ 的值域位于某个 $\operatorname{Ran}B^r$。也没有把原未修正 $G_0v-Jv$ 宣称为核向量。

取真实 $f\in\mathcal N^\perp$，令 $T^*h=f$ 为其规范逐行形式原像。对有限 $v\in\Pi\mathcal H$，
$$
\langle h,v\rangle
=\langle f,Jv\rangle
=\langle f,G_{\rm reg}v\rangle.
$$
密度及 Riesz 表示给
$$
\boxed{
\Pi h=G_{\rm reg}^*f,
\qquad
\|\Pi h\|\le(1+e^{-39u^4})\mathcal B_s(x)\|f\|.
}
\tag{4.2}
$$
尤其未变的原有限列满足
$$
\boxed{
\|\Pi h-G_0^*f\|
\le e^{-39u^4}\mathcal B_s(x)\|f\|.
}
\tag{4.3}
$$
更精确地，完整共同误差就是
$$
\Pi h-G_0^*f=-E^*G_{7\to3}^*f,
\tag{4.4}
$$
其中 $G_{7\to3}^*$ 按 $\mathscr X_3$ 与 $\mathscr X_7$ 的 Banach 对偶理解，最后由 $E^*$ 回到窗口 Hilbert 空间。若不使用 Banach 伴随记号，同式准确地定义为有界 Hilbert 算子 $-(G_{7\to3}E)^*f$。后者不需要为 $G_{7\to3}$ 赋予未证明的全 Hilbert 定义域。

(4.2)–(4.3) 对原 $f=w\in W$ 可直接使用，并且完全保留同一个 $G_0$、同一个 $m,x$ 和两个物理孔截断。它们不是将前稿的完整 MP 自然域假定扩为形式序列；合法性来自 (4.1) 的稳定范围差。

## 5. 对后续返回配对保留的限制

本文实付的是“原有限 Neumann 列—规范形式 forcing”的误差；不只提供另一个小范数平均代表。该式可在后续同源计算中使用 $G_0^*f$，其误差为 (4.3)，无需把原来源换成高位平均列。

但 $G_0^*f$ 仍含完整 $\mathcal Q_x^*$ 与 $C^*$ 幂的相互作用。它没有将 $P_{\widehat{\mathscr E}}$ 或零源核 Schur 删除，也没有使该投影保持早孔截断。对于仅知趋零的原尾范数，$\mathcal B_s(x)$ 的增长仍须另付。形式 $h$ 的全局平方和、同 $W$ 的普通封口与返回主配对继续开放。
