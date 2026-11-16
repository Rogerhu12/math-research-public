# R271 附录：并行一位完整 Schur 的共同头恢复及真实压后 creation 行

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 固定同一个强头 $C$，分别只把每个远位 $i$ 加为硬核位。所有新位的占据源 $a_{1,i}$ 都处于原共同头空间。完整正 Schur 给这些源的平方可和预算；已付 coherent 来源 Gram 再支付恢复后的 $H_i a_{1,i}$，不估 $\|H_i\|$。由此得到一条明确的实际压后 creation 行，并能接原不同 head 来源的合成行。

这与把不同前缀的源强行放入同一个远真空 forcing 空间不同。全部来源和每个新增位的原物理 cut 在下文逐项保留。结论仍不等于固定 $u_f$ 的删除范数行，也不删除原投影返回。

依据：

- [一位完整 Schur 与自然域](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)；
- [正 commutator 因子及整段真实新源](R271-appendix-one-bit-positive-commutator-and-complete-moving-source-occupation-row.md)；
- [完整 coherent 同源列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)；
- [原不同来源的 creation 合成行](R271-appendix-actual-forcing-continuous-tail-occupation-potential-and-source-schur-readout.md) §4，以及其前稿的 $Z_V/Z_K$ 版本。

## 1. 固定共同头，分别硬化各远位

令
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0,
$$
$$
D=\sum_{i\ge x}b_iE_i,\quad b_i=(i+1)^{-2},\quad
z_i=b_i^2,\quad S=\sum_{i\ge x}z_i.
\tag{1.1}
$$
固定原允许的强头 forcing 空间 $\mathcal F$，$i_0$ 将它嵌入远尾真空。原
$$
K=K_{m,Q}\subset V=V_{m,Q},\quad
P_U=P_V-P_K,\quad Z_E=P_Ei_0\ (E=V,K,U),\quad G_E=Z_E^*Z_E
$$
始终不换。取
$$
Q\ge R+h+1
\tag{1.2}
$$
足以覆盖下文全部来源及新增一位的完整塔；该条件不含远位的数值位置 $i$。

对辅助方差 $t\in[S,2S]$，置
$$
s_i=S+t-z_i>S,\qquad C_i=C+b_iE_i,\qquad C_i^{h+1}=0 .
\tag{1.3}
$$
这里每个 $i$ 都单独从同一个 $C$ 出发，而不是依次把其它远位并头。新头为 $\mathcal F\otimes\mathbb C^2$；所有 $a_{1,i}$ 仍属于原 $\mathcal F$。

在同一全尾 Fock 空间中保额外方差 $t$ 的 mode。旧闭核是
$C+D_{\rm bos}+\sqrt t\,a_{\rm extra}$ 的核；第 $i$ 个新闭核只额外限制该位占据至多 $1$。它是旧核的闭子空间。旧投影平方为
$$
q(S+t)=\langle g,H_C(S+t)^{-1}g\rangle .
$$
新投影以全部新头源 $(a_{0,i},a_{1,i})$ 最小化，平方记为 $q_{{\rm new},i}(t)$。一位正因子定理给
$$
\boxed{
G_i(t):=q_{{\rm new},i}(t)-q(s_i)
=\|H_i^{1/2}a_{1,i}\|^2+
u_i\|\mathcal K_i^{1/2}H_i^{1/2}a_{1,i}\|^2\ge0,
}
\tag{1.4}
$$
其中
$$
H_i=H_C(s_i),\qquad u_i=z_i/s_i,\qquad
T_i=H_i^{1/2}CH_i^{-1/2}/\sqrt{s_i},\qquad
\mathcal K_i=I+T_i^*T_i-T_iT_i^*\succeq0.
$$
精确新源而非候选为
$$
H_i^{1/2}a_{1,i}
=-\sqrt{u_i}(I+u_i\mathcal K_i)^{-1}
 T_iH_i^{-1/2}g.
\tag{1.5}
$$
全部乘积在已付有限 Fock 次数自然域上定义。这里不涉及任何远尾 Moore--Penrose 逆。

## 2. 一次参数选择支付整个无限新位源行

嵌套核给
$$
0\le G_i(t)\le q(S+t)-q(S+t-z_i).
$$
定义原共同头上的正算子
$$
\mathcal V=
H_C(3S)^{-1}-H_C(2S-z_x)^{-1}\succeq0,
\qquad V_g=\langle g,\mathcal Vg\rangle .
\tag{2.1}
$$
对每个 $i$ 用非负导数作 Fubini，得到
$$
\int_S^{2S}[q(S+t)-q(S+t-z_i)]\,dt
\le z_i[q(3S)-q(2S-z_i)]
\le z_i V_g .
$$
对有限子族求和，再由 Tonelli 及 $\sum_i z_i=S$，有
$$
\boxed{
\frac1S\int_S^{2S}\sum_{i\ge x}G_i(t)\,dt\le V_g.
}
\tag{2.2}
$$
因此对每个固定 $g$，存在同一个 $t_*\in[S,2S]$ 使
$$
\boxed{
\sum_{i\ge x}
\left[
\langle H_i a_{1,i},a_{1,i}\rangle+
u_i\|\mathcal K_i^{1/2}H_i^{1/2}a_{1,i}\|^2
\right]\le V_g.
}
\tag{2.3}
$$
所有 $H_i,a_{1,i}$ 以后均取这个共同 $t_*$。可取 Lebesgue 意义下的一个满足该界的点；每个单列连续，而非负无穷和可测，积分有限已保证这样的点存在。若 $V_g=0$，无穷行几乎处处严格为零。

这一步未对每个远位分别选方差，也未将完整 $H_i$ 换成共同标量。积分形式对每个 $g$ 成立，所以本身是整个共同 forcing 空间上的正算子不等式。

## 3. 原 coherent 源 Gram 支付完整恢复

对任意 $s\ge S$，定义标准**全远尾**物理列
$$
\mathcal R_s a
=\sum_{j=0}^{h-1}
\frac{(-C)^ja\otimes(D^*)^j\Omega}{s^j j!}.
$$
已付同源身份与物理范数界给
$$
P_E\mathcal R_s a=Z_EH_C(s)a,\qquad
\|\mathcal R_s a\|^2\le\langle H_C(s)a,a\rangle,
\quad E=V,K,U .
\tag{3.1}
$$
这些身份对全部头 $a$ 成立，并未压到 $g$ 的旧支持。故
$$
H_C(s)G_EH_C(s)\preceq H_C(s),\qquad
\boxed{G_E\preceq H_C(s)^{-1}.}
\tag{3.2}
$$
这是从原物理投影先得到二次型，再作合法完整 inverse 同余；不假设 $G_E$ 可逆。

现在每个 $s_i>S$，因此 (3.2) 适用于 $H_i$，且使用同一个原 $Z_E$。令恢复后的共同头来源为
$$
r_i=H_i a_{1,i}\in\mathcal F.
\tag{3.3}
$$
于是
$$
\boxed{
\sum_{i\ge x}\|Z_Er_i\|^2
\le\sum_{i\ge x}\langle H_i a_{1,i},a_{1,i}\rangle
\le V_g,\quad E=V,K,U.
}
\tag{3.4}
$$
恢复 $H_i$ 的费用已经由真正的投影源 Gram 支付，不需要
$\|H_i\|\,\|a_{1,i}\|$。本节没有断言
$\sum_i\langle G_\Delta r_i,r_i\rangle\le V_g$；
$G_\Delta=I-G_U$ 不是 (3.2) 的左边。

另一方面，(3.1) 给
$G_U\preceq H_C(2S-z_x)^{-1}$，而
$H_C(3S)^{-1}\preceq I$。所以
$$
\boxed{\mathcal V\preceq I-G_U=G_\Delta,\qquad
V_g\le\|i_0g-u_g\|^2.}
\tag{3.5}
$$
因此 (3.4) 的最终右端仍是同一个原缺陷，而不是一个新选的 forcing 费用。积分形式可再作任意共同来源合同，保真实 $R^*\mathcal V R$。

## 4. 逐列真实压后 creation 返回的识别

令
$$
D_{\widehat i}=D-b_iE_i.
$$
第 $i$ 个新核的物理压缩为
$$
F_i=
\sum_{j=0}^{h}
\frac{(-C_i)^j(a_{0,i},a_{1,i})
      \otimes(D_{\widehat i}^*)^j\Omega}{s_i^j j!}.
\tag{4.1}
$$
新增位不连续也不影响原总孔 cut：它只增加一个物理位，
$C_i$ 只删除强位或作用于原 $A_m$，远尾删除作用于其余位；
所以 (1.2) 保完整 $R+1+h$ 支持。这里不假设原 $V_{m,Q}$ 对 $C_i$ 或单个 $E_i$ 不变，逐列来源直接由真实低 forcing 恒等式证明。令 $i_{0,i}$ 嵌入全部新头且其余远尾真空。因 $C_i^*$ 与 $D_{\widehat i}^*$ 作用于不同张量因子，
$$
(D_{\widehat i}^*)^j-(-C_i^*)^j
=L_m^*\sum_{k=0}^{j-1}
(D_{\widehat i}^*)^{j-1-k}(-C_i^*)^k.
\tag{4.1a}
$$
右端作用于 $i_{0,i}z$ 后，每个中间列的原总尾孔数至多
$R+1+(j-1)=R+j$；旧头 $A_m^*$ 不计入这个尾孔数，其余每个创建至多加一孔。对 $j\le h$，(1.2) 给 $R+j\le Q-1$。原 $V_{m,Q}$ 的定义是 $\Pi_{<Q}L_mv=0$，故准确有
$P_VL_m^*\xi=0$ 对所有这些中间列 $\xi$；真核 $K$ 的同一身份也成立。这就逐列得到
$P_E(D_{\widehat i}^*)^ji_{0,i}=(-1)^j(P_Ei_{0,i})(C_i^*)^j$
（$E=V,K$），而非把 $C_i$ 移过原投影。代入完整 $H_{C_i}(s_i)$ 的源方程，故
$$
P_VF_i=P_Vi_0g,\qquad P_KF_i=P_Ki_0g,\qquad P_UF_i=u_g .
\tag{4.2}
$$
这是同一个原 $u_g$，并没有把新增第 $i$ 位换成原的新 cut。

在新增位的 bit-$1$ 行，$C_i^j(a_{0,i},a_{1,i})$ 的分量是 $C^ja_{1,i}$。故
$$
E_iF_i=
\sum_{j=0}^{h-1}
\frac{(-C)^ja_{1,i}\otimes(D_{\widehat i}^*)^j\Omega}
     {s_i^j j!},
\qquad
\|E_iF_i\|^2\le\langle H_i a_{1,i},a_{1,i}\rangle .
\tag{4.3}
$$
特别 $\sum_i\|P_U E_iF_i\|^2\le V_g$。

应用完整 $2\times2$ 新头 Gram，而不是移 $E_i$ 过投影：
$E_i(a_{0,i},a_{1,i})=(a_{1,i},0)$。其完整 Gram 像准确为
$$
H_{C_i}(s_i)\binom{a_{1,i}}0
=\binom{H_i a_{1,i}}{(b_i/s_i)H_iCa_{1,i}}.
$$
因此得到真正来源识别
$$
\boxed{
P_U E_iF_i
=Z_U r_i+
\frac{b_i}{s_i}P_U E_i^*i_0H_iCa_{1,i}.
}
\tag{4.4}
$$
两个右项都在原物理环境上，$C$ 与 $C^*$ 的角色未互换。结合 (3.4)、(4.3) 的整行平方，得
$$
\boxed{
\sum_{i\ge x}
\left\|\frac{b_i}{s_i}P_U E_i^*i_0H_iCa_{1,i}\right\|^2
\le4V_g.
}
\tag{4.5}
$$
这是一条确切的压后 creation 行；它的 head 来源由完整新位 Schur 指定，不是任意环境列。权 $b_i/s_i$、恢复次序 $H_iC$、外层 $P_U$ 都必须保留。

## 5. 接旧不同来源合成行而不误用缺陷 Gram

旧正 Gram 对 $Z_V$ 和 $Z_K$ 各给
$$
\left\|\sum_i\frac{E_iZ_E g_i}{\sqrt{i+1}}\right\|^2
\le\frac43\sum_i\langle G_Eg_i,g_i\rangle,
\qquad E=V,K.
\tag{5.1}
$$
精确入口是[实际低端 forcing 正 Gram 稿](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md) §1(1.1)、§3b(3b.4)：其中 $Z$ 明确可取 $Z_V,Z_K,Z_e$，并对每个这样的 $Z_E$ 给
$\sum_i E_iP_{\operatorname{Ran}Z_E}E_i^*/(i+1)\preceq4I/3$。
置 $T_i=E_iZ_EG_E^{\dagger/2}/\sqrt{i+1}$，则该式就是
$\sum_iT_iT_i^*\preceq4I/3$。又 $\ker G_E=\ker Z_E$，
所以 $T_iG_E^{1/2}g_i=E_iZ_Eg_i/\sqrt{i+1}$，准确推出 (5.1)；
这里不使用互补 Gram $I-G_E$，也不假设 $G_E$ 可逆。

此处全部 $g_i$ 位于同一个原强头 $\mathcal F$，所以可取 $g_i=c_i r_i$。对任意有界标量族 $(c_i)$，(3.4) 给
$$
\boxed{
\left\|\sum_{i\ge x}
\frac{c_iE_iZ_Ur_i}{\sqrt{i+1}}\right\|^2
\le\frac{16}{3}\,\sup_i|c_i|^2\,V_g.
}
\tag{5.2}
$$
证明先分别对 $Z_V,Z_K$ 使用 (5.1)，最后只用
$\|a-b\|^2\le2(\|a\|^2+\|b\|^2)$。
因此真实 $V/K$ 两分量及其相减始终保留，没有将其共同能量替换为
$\|Du_g\|^2$。无穷合成按 (5.1) 的平方可和自然域收敛。

这里用的是被 (3.2) 支付的 $G_V+G_K$ 来源，而非声称
$G_\Delta\preceq H_i^{-1}$。后一声称既未使用，也没有由本稿证明。

## 6. 原窗口和仍未支付的返回

取 $R=d$、$x=m+d$、$h=2d$，充分大的 $m$ 下原母窗
$4d\le Q\le e^{26d^3}$ 满足 (1.2)。端点
$3S$、$2S-z_x$ 都不小于真实 $S=S_x$，并趋零。
原强前缀完整 Gram 定理给
$$
V_g=q(3S)-q(2S-z_x)\longrightarrow0
$$
对每个固定原物理 forcing 成立。参数选择先于全部这些 $Q$，所以
(3.4)、(4.5)、(5.2) 都在同一来源上成立。

这些是 restored head 来源、其真实压后 creation 返回及合法合成行的预算。
它们仍不把
$$
E_i u_g=P_U E_iF_i+
\left[E_iP_UF_i-P_U E_iF_i\right]
$$
中方括号的原投影返回删掉。
也未把 $F_i$ 的物理压缩称为真核，未将不同 $i$ 的完整新源视为一条公共兼容塔。原全部深返回、两个 partial 及 same-$w$/carry 接口继续保留；$N=M$ 尚未由本稿完成。
