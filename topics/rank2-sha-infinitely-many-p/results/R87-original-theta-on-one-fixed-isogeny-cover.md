# R87：原 theta 对角在同一个固定同源覆盖上的模型

日期：2026-11-12。状态：固定标签、平移补偿、有理下降及完整对角均已根端独审。
完整证明见[平移 Kummer 单位与原 theta 覆盖](../notes/2026-11-12-translated-kummer-units-and-original-theta-cover.md)。

固定原 $E:y^2=x^3-17x$、$N=68$、$F=K(E[f])$、原 $256$ 点轨道
$\mathcal S$ 及参考二挠点 $T=(0,0)$。变量 $z,w$ 均是纤维加法参数。

## 1. 保留原 theta 所需的公共因子和非线性

在原方格纤维，令
$F_P(z)=e^{-\eta_Pz}\sigma(z_P+z)/\sigma(z_P)$、
$T_N(z)=\sigma(Nz)/(NZ(z))$。
实际原函数及原系数为

$$
\Theta_P(z,w)=\frac{F_P(z+w)}{F_P(z)\sigma(w)},\qquad
d_m=[z^mw^m]\left(\sum_{P\in\mathcal S}\Theta_P(z,w)-\frac{256}{w}\right).
$$

归一单位准确满足 $r_P=T_NF_P^{-N^2}$，从而

$$
[\sigma(w)\Theta_P(z,w)]^{N^2}
=\frac{T_N(z+w)/T_N(z)}{r_P(z+w)/r_P(z)}.
$$

必须逐标签取原点值一的根后再相加。
非 CM 纤维使用普通 sigma 时，右侧另有
$\exp(-N^2s_2zw)$；该公共因子在两个标签之比中消去。

## 2. 覆盖和系数域均固定

唯一有理函数 $B_P\in F(E)^\times$ 由

$$
\operatorname{div}B_P=N(-P)-N(-T),\qquad B_P(O)=1
$$

确定，并有 $B_P^N=r_T/r_P$。
同一个 $[N]$ 覆盖同时消去所有根：

$$
A_P(z)=\frac{F_P(Nz)}{F_T(Nz)}
=B_P([N]z)^{1/N}\in F(E)^\times,
$$
$$
\operatorname{div}A_P=[N]^*(-P)-[N]^*(-T),\qquad A_P(O)=1.
$$

有理性由准周期或 Picard 判据证明；规范除子下降给原 $F$，
不需扩大到 $F(E[N^2])$。
在好位 $p\nmid2\cdot17$，这些函数的原点 germ 均为整单位。
参考 theta 自身的分母与半径没有被消去。

于是原始对角准确恢复为

$$
N^{2m+1}d_m=[z^mw^m]
\left\{N\Theta_T(Nz,Nw)
\sum_{P\in\mathcal S}\frac{A_P(z+w)}{A_P(z)}-\frac{256}{w}\right\}.
$$

$N^{2m+1}$ 包含 theta 的一次伸缩，且在所有目标素数处为单位。

## 3. 平移范数常数没有提供独立中央项

正确的平移单位是 $\widetilde r_P(W,R)=r_P(W+R)/r_P(W)$。
其范数常数依赖 $W$，全部子群的乘积准确给

$$
\kappa_{[p],P}(W)
=\kappa_{[p],P}\frac{r_{pP}([p]W)}{r_P(W)^{p^2}}.
$$

其正 $W$ 阶导数已写回原单位导数；所有同时含正 $R$ 阶的混合导数
仍杀掉 $\log\kappa(W)$。
真实比值 $\mathcal R_{P,T}=\Theta_P/\Theta_T$ 满足完整乘法分配

$$
\prod_G\mathcal R^{E/G}_{\varphi_GP,\varphi_GT}(c_Gz,c_Gw)
=\mathcal R^E_{P,T}(z,w)^p\mathcal R^E_{pP,T}(pz,pw).
$$

它不是原来 $256$ 项之和的线性关系。甚至首个对角已经有
$[zw]\Theta_P=-U_Px(P)-y(P)$；其中 $-U_Px(P)$ 来自指数化乘积。
因此不能用范数的对数和替代完整对角。
现有固定覆盖模型尚须与真实中央配对及全部 Frobenius 深度接合，
无穷素数非零性仍未证明。
