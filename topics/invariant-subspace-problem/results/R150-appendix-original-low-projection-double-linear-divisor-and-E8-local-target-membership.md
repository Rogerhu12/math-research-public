# R150 补篇：原低投影的双线性确定因子下界与 E8 局部目标来源

日期：2026-11-15 UTC。作者：Astra-ISP-789f / literature_audit。AI 辅助：GPT-6 Astra Pro。

状态：解析证明。只用原物理方程、原多项式单位变换和已证明的 $D_{\mathrm{lin}}$；不使用未完成的 E8 Schur 运算。证明完整 $51\times36$ 低投影在每个相关局部环中的扭子长度至少为原九维横向线性块长度的两倍。于是 E8 的全部八个共轭点上，原九个 $h_0t_j$ 的局部来源已经成立。

## 1. 结论及原矩阵

沿用
$$
\begin{aligned}
F_+&=5s^3-25s^2+32s-8,\\
F_-&=5s^3+135s^2+864s+864,\\
E_8&=5s^8+50s^7+153s^6-936s^5-2888s^4
       +15936s^3-3392s^2-25472s+9600,
\end{aligned}
$$
以及原共同候选
$$
h_0=s^3(s-2)F_+^2F_-^2E_8.
$$
原线性块的精确确定因子为
$$
D_{\mathrm{lin}}
=s^8(s-2)^2(s+6)^2F_+^3F_-^3E_8^2.
\tag{1.1}
$$
这是[原线性块的全部九阶子式 gcd](R150-appendix-exact-characteristic-zero-linear-divisor-and-minimal-inverse.md)，不是某个未经核实的子式。

令 $R=\mathbb Q[s]_{(F)}$，其中 $F=F_+,F_-$ 或 $E_8$。低矩阵 $S$ 为原十七式乘 $1,c,d$、取纯次数至多三和横向次数一且切向次数至多一的 $51\times36$ 原矩阵。令 $\delta_S$ 为其正 Smith 指数之和。则
$$
\boxed{\delta_S\ge2v_F(D_{\mathrm{lin}}).}
\tag{1.2}
$$
特别地，
$$
\delta_{S,F_\pm}\ge6,\qquad \delta_{S,E_8}\ge4.
\tag{1.3}
$$

令 $A:R^{6188}\to R^{4367}$ 为原完整有限来源矩阵，$L=\operatorname{im}A$，
$$
W=(z_2,\ldots,z_{10})^2_{\le5},\qquad\operatorname{rank}W=4212,
$$
$P$ 为全部真实原来源模 $W$ 的 $224\times155$ 投影矩阵。原低 jet 的零扩展给 $\delta_P\ge\delta_S$，而既有全块模 $31$ 证书给 $\delta_{A,E_8}\le5$。因此
$$
\boxed{4\le\delta_{P,E_8}\le\delta_{A,E_8}\le5,\qquad
       \ell_R\bigl(W/(L\cap W)\bigr)\le1.}
\tag{1.4}
$$
所以
$$
\boxed{E_8W\subset L,\qquad h_0t_j\in L\quad(2\le j\le10).}
\tag{1.5}
$$
本篇不声称 E8 的完整长度恰为四或五。

## 2. 低矩阵的原物理三层表示

记
$$
y=v(s),\quad u=v'(s),\quad Y=y^2,\quad
T=yu^T+uy^T,\quad p=Ky,\quad q=Ku,\quad r=Kv''(s),
$$
$$
g=u^TKu=-2s^2(s-2)(s+6).
$$
$K$ 始终为原六维矩阵。$J_2,J_3$ 为原物理平方、立方配对矩阵。
$$
L_y=J_3^{-1}B_yJ_2,\qquad A_yM=(L_yM)_p,
$$
其中 $B_y$ 为乘以 $k_s(z)=y(s)^TKv(z)$ 的原系数矩阵。

原 Hankel 配对为
$$
\langle X,Z\rangle_K=\operatorname{tr}(KXKZ).
$$
$A_y$ 自伴随，$A_yY=A_yT=0$。原二项式平移矩阵
$$
\mathcal T(s)_{nj}=\binom nj s^{n-j}\quad(j\le n)
$$
的行列式为一，其列为 $Y,T$ 以及九个正常向量 $\mathcal N_j$。置
$$
\mathcal N=\operatorname{span}_R\{\mathcal N_2,\ldots,\mathcal N_{10}\}.
$$
这是实际多项式直和
$$
\mathcal H_2=RY\oplus RT\oplus\mathcal N.
\tag{2.1}
$$

低右坐标除六个恒等纯核列外，可记为
$$
t_0,t_c,t_d;\qquad w_0,w_c,w_d\in\mathcal N.
$$
前三者分别读取 $d^2,cd^2,d^3$；后三组分别读取 $z_j,cz_j,dz_j$。
原 $N$ 方程的三组低输出，取回唯一 Hankel 极线代表后，准确为
$$
B_c=6A_yw_c+4g t_cY,\qquad
B_d=6A_yw_d+4g t_dY,
\tag{2.2}
$$
$$
B_0=6A_yw_0+4g t_0Y+E(w_c,w_d),
\tag{2.3}
$$
其中
$$
E(w_c,w_d)
=4\Pi(YKw_c+w_cKY+TKw_d+w_dKT).
\tag{2.4}
$$
$\Pi$ 是原极线投影，满足对 Hankel $X$ 有
$\langle X,\Pi Z\rangle_K=\langle X,Z\rangle_K$。原十一条 $N$ 的系数向量是上述 Hankel 向量乘固定可逆 $J_2$；没有增加额外矩阵条目方程。

六条原 $\Gamma$ 在这组低坐标上的输出为
$$
\Gamma_{\mathrm{low}}
=-12(A_yw_c)p-24(A_yw_d)q
=-2B_cp-4B_dq,
\tag{2.5}
$$
因为 $Yp=Yq=0$。这是完整六维原均值梯度。其 $c,d$ 倍行在当前低列上恒为零。式 (2.5) 亦可直接从原
$$
\Gamma(M)=2\operatorname{tr}(KMKM)y+8MKMp
          -12(L_yM)_{KMK}
$$
双线性展开得到：$Y$ 的交叉项为 $-12(A_yZ)p$，$T$ 的交叉项为 $-24(A_yZ)q$。

## 3. 两个顶端切向行也是底层的真实行组合

先由 $YKY=YKT=TKY=0$ 得
$$
\langle Y,E(w_c,w_d)\rangle_K=0.
\tag{3.1}
$$
又有 $(KT)^2=gpy^T$，所以
$$
\langle T,E(w_c,w_d)\rangle_K=8g\,p^Tw_dp.
\tag{3.2}
$$

为把右端写成实际底层行，使用原最高恒等式
$$
(L_yw)(Kv(z),Kv(z),Kv(z))
=k_s(z)\,w(Kv(z),Kv(z)).
\tag{3.3}
$$
在 $z=s$ 取二阶 Taylor 系数。由 $k_s(s)=k_s'(s)=0$、$k_s''(s)=-g$，得到
$$
-\frac g2p^Twp
=3q^T(A_yw)q+\frac32p^T(A_yw)r.
\tag{3.4}
$$
将 (3.4) 用于 $w_d$，并代入 $B_d$，因 $q^TYq=p^TYr=0$，得到不含任何 $1/g$ 的多项式行恒等式
$$
\boxed{
\langle T,B_0\rangle_K
=-8q^TB_dq-4p^TB_dr.
}
\tag{3.5}
$$
同时
$$
\langle Y,B_0\rangle_K=0,\qquad
\langle Y,B_c\rangle_K=\langle T,B_c\rangle_K
=\langle Y,B_d\rangle_K=\langle T,B_d\rangle_K=0.
\tag{3.6}
$$

因此，不能只把 (3.5) 理解为在底层核上成立的点值关系；它是原矩阵所有列上的精确行组合。

## 4. 全部 $51$ 行通过单位行变换降为 $27$ 行

在每组三个 $N$ 输出上使用
$$
Z\longmapsto\mathcal T(s)^TJ_2 Z.
$$
这是多项式单位行变换，最前两行恰为 $\langle Y,Z\rangle_K$、$\langle T,Z\rangle_K$。

先按 (2.5) 消去六个 $\Gamma$ 行；其余十二个 $\Gamma$ 乘子行已恒零。三组 $N$ 的六个切向行再按 (3.5)、(3.6) 消去：底层四行和顶层 $Y$ 行恒零，顶层 $T$ 行是底层的精确组合。故存在 $R$ 上的可逆行变换，把完整低矩阵变为
$$
S\ \sim_R\
\begin{pmatrix}\mathscr S\\0_{24\times36}\end{pmatrix},
\qquad \mathscr S:R^{36}\to R^{27}.
\tag{4.1}
$$
这一步保留了全部原行。它不是只取一个 $27$ 行子矩阵后忽略剩余行。

限制输入到 $w_0,w_c,w_d$ 的二十七个正常坐标，得到块上三角的 $27\times27$ 子矩阵，其三个对角块均为下文的 $H$。由原线性确定因子定理，$\det H$ 在函数域非零，故该子式为 $(\det H)^3\ne0$。结合 (4.1) 的二十七行上界，直接得到原低矩阵泛秩恰为 $27$。因此 $\mathscr S$ 泛满行，
$$
\operatorname{coker}S\cong R^{24}\oplus\operatorname{coker}\mathscr S,
$$
且 $\operatorname{coker}\mathscr S$ 是有限扭子模。

## 5. 用原二阶物理 jet 消去底层的纯列

下面给出真实局部整提升，避免仅由逐点像成员性作推断。

令
$$
V_2(s)=\frac12\frac{d^2}{ds^2}v_{15}(s),
$$
即原物理立方序列的二阶 Taylor 列。其原极线多项式为
$$
J_3V_2
=\frac12\partial_s^2(k_s^3)
=k_s\left(3(\partial_s k_s)^2+\frac32k_s\partial_s^2k_s\right).
$$
所以原 Hankel 多项式列
$$
M_2
=J_2^{-1}
\left[3(\partial_s k_s)^2+\frac32k_s\partial_s^2k_s\right]
\tag{5.1}
$$
满足 $L_yM_2=V_2$。在固定 $p=Ky$ 下收缩，或对
$B_y^Tv_{15}(z)=k_s(z)v_{10}(z)$ 取二阶 Taylor 系数，得到
$$
\boxed{A_yM_2=-\frac g2Y.}
\tag{5.2}
$$
从 $M_2$ 扣除其在 (2.1) 中的 $Y,T$ 分量，记正常部分为 $M_{2,\mathcal N}$。置
$$
\tau=-\frac43M_{2,\mathcal N}.
$$
于是
$$
6A_y\tau=4gY.
\tag{5.3}
$$
所有系数属于 $R$；实际上只用固定非零有理分母，并未除去可能消失的 $g$。

分别作可逆三角列变换
$$
\widetilde w_c=w_c+\tau t_c,\qquad
\widetilde w_d=w_d+\tau t_d.
$$
两底层输出就变成
$$
B_c=6A_y\widetilde w_c,\qquad
B_d=6A_y\widetilde w_d.
\tag{5.4}
$$
其他顶层输出会随此列变换改变，全部保留；证明不需要估计或丢弃这些改变。

令 $H$ 为 $6A_y|_{\mathcal N}$ 在上节九个正常输出坐标中的 $9\times9$ 矩阵。原 $D_{\mathrm{lin}}$ 定理使用的补空间与本补空间都由多项式单位基得到，两者间的正常坐标矩阵为行列式一的三角矩阵。因此
$$
v_F(\det H)=v_F(D_{\mathrm{lin}}).
\tag{5.5}
$$
固定 $J_2,\det J_3$ 或 $6$ 的非零有理倍数不影响局部赋值。

## 6. 有限扭子模满射给出两倍长度

在完成 (4.1) 和上述列变换后，把 $\mathscr S$ 的 $27$ 个输出投到两底层的 $18$ 个正常输出。其来源像准确为
$$
\operatorname{im}(H\oplus H)\subset R^{18},
$$
因为其余列在这两底层上为零，而 $\widetilde w_c,\widetilde w_d$ 是独立自由输入。故有满射
$$
\boxed{
\operatorname{coker}\mathscr S
\twoheadrightarrow
\operatorname{coker}H\oplus\operatorname{coker}H.
}
\tag{6.1}
$$
左右均为有限扭子模。左端不存在一个未控制的自由部分来替右端扭子提供原像；这正是必须先完整支付第 4 节的原因。因此
$$
\delta_S=\ell_R(\operatorname{coker}\mathscr S)
\ge2\ell_R(\operatorname{coker}H)
=2v_F(D_{\mathrm{lin}}).
$$
这证明 (1.2)。顶层的两个混合块没有删掉，它们仅不改变向真实两底层余核的满射。

## 7. E8 因子与原九目标

将 (1.1) 代入上式，得 $\delta_{S,E_8}\ge4$。
[两三次数域低 jet 注入证明](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md)
第 2、4 节的原多项式零扩展恒等同样适用于 E8：低核加四个不交的恒等纯核坐标嵌入全部 $224$ 个原投影行，且自由项 $9+4=13$ 恰好抵消。因此 $\delta_{P,E_8}\ge4$。

原 E8 不可约、其所有根的完整常秩 $4352$、泛秩 $4354$，以及全块模 $31$ 的长度上界五，见
[E8 完整分类](R150-appendix-rank-one-E8-means-complete-critical-classification.md)、
[E8 不可约性](R150-appendix-rank-one-E8-irreducibility-and-good-residue-root.md)、
[完整仿射扭子因子](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)。
原完整泛型像包含 $W$，故真实环境商的精确序列给
$$
\ell_R\bigl(W/(L\cap W)\bigr)=\delta_A-\delta_P\le1.
$$
所以 $E_8W\subset L$。原
$$
t_j=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2=z_j^2
$$
确在 $W$，并且 $h_0/E_8$ 在 E8 局部为单位。于是 (1.5) 成立，覆盖全部八个复共轭根。

作为另一个同原整数整块的推论，全部最大子式在 $\mathbb Q[s]$ 中均被 $E_8^4$ 整除。$E_8$ 的首项系数 $5$ 是 $31$ 单位，所以除式在 $\mathbb Z_{(31)}[s]$ 中仍合法。既有模 $31$ 分解
$$
\overline E_8=5(s-2)(s-1)E_6
$$
使原 $s=2$ 的模上界 $32$ 至少下降四：
$$
\boxed{\delta_{A,2}\le28.}
$$
与已经实际付清的 $\delta_{P,2}=12$ 合并，仅得
$$
\ell_{\mathbb Q[s]_{(s-2)}}\bigl(W/(L\cap W)\bigr)\le16.
$$
这还没有支付原 $h_0$ 在 $2$ 点只有一次的目标来源；不将该剩余问题视为已关闭。

本篇全部新结论来自上列原式恒等、单位变换、有限模满射及既有精确线性确定因子。继续进行的真数域 Schur 可给更精确的低谱，但不是本篇 E8 局部成员性的前提。

## 8. 合并全部已付有限点后的公共因子和条件费用

把本篇 $E_8^4$ 下界、两个三次因子的六次下界，以及已完成二点投影长度 $12$ 一并纳入原全部最大子式公共因子，得
$$
K_{158}=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,\qquad
\deg K_{158}=158.
$$
二点的指数十二来自 $\delta_A\ge\delta_P=12$，不要求二点目标成员性已经解决。本式首项为 $5^{16}$，是 $31$ 单位。

保留同一选定 $D$、总权 $8770$、已经证明的无穷远界 $130/125/125$ 及模 $31$ 次数 $8527$，仍有
$$
8527\le\deg D\le8640,\qquad
8369\le q:=\deg(D/K_{158})\le8482.
$$
沿[三次因子补篇第七节](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md)的同一三支公式，费用为
$$
\begin{aligned}
\text{非基来源}&\le8482-1+45=8526,\\
\text{原来源转移}&\le8770+55-125-158-11=8531,\\
\text{目标伴随支路}&\le8770+64-125-158-10-8369=172.
\end{aligned}
$$
故原九目标在全局 $\mathbb Q[s]$ 来源成员性成立的前提下，统一费用至多 $8531$。剩余的二点局部目标条件、未知异常支持及固定 $D$ 首项的 $31$ 单位条件没有由本篇补足。
