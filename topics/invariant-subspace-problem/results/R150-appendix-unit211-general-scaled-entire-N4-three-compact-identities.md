# 全原 N4 的三个无分母缩放系数

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：完整原多项式恒等式。** 本条给出整个原值二次型 N4 的三个短式。只使用对称规范 p+q=2；不假定 W、Phi、原均值方程或 D 非零。三个式是九个独立原变量中的多项式恒等式，ell=0 亦保留。它们可在旧 native 原归约器的分母范围内处理完整值向量。

## 1. 自由原 Gram

取九个独立变量 $b,c,\rho,A_1,r,s,t,\lambda,T$，令
$$
\ell=b+c,\quad a=1-\ell,\quad p=1+\rho,\quad q=1-\rho,
\quad Q=1-\rho^2,\quad \delta=\rho^2.
$$
原四行是
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad g_C=(q,s,t,0).
$$
使用真正的 double-germ 乘法及迹
$$
(vz)_0=v_0z_0,\quad (vz)_1=v_0z_1+v_1z_0,\quad
(vz)_B=v_Bz_B,\quad(vz)_C=v_Cz_C,
$$
$$
\tau(v)=av_0+v_1+bv_B+cv_C.
$$
令 $\mathbf1=(1,0,1,1)$，$\mathcal Kv=(\tau(g_jv))_j$，
$d=\mathcal K\mathbf1$，$2f=\tau(d)$。写
$$
d=(u,d_1,X,Y),\quad u=bp+cq,\quad
X=ap+r+ct,\quad Y=aq+s+bt,
$$
$$
\mathcal V=bX+cY,\quad \mathcal W=bpX+cqY,\quad
m=u-\ell=\rho(b-c),\quad M=4bc\delta.
$$
完整原二次型为
$$
N_4(v)=2\tau(dv^2)-2f\,\tau(v^2)
-4\tau(v)\tau(dv)+4f\,\tau(v)^2+\tau(v\mathcal Kv).
\tag{1}
$$
(1) 对 v 齐次二次，不使用任何错误的 double-germ 平方替代式。

## 2. 三个完整多项式系数

定义
$$
w=\lambda-1-T,\quad c_\lambda=3-2\lambda,\quad
A_\lambda=2\lambda^2-2\lambda+1,\quad D=\ell A_\lambda-T^2.
$$
这里 D 首先只是自由多项式；只有原值矩条件成立时才解释为物理 D。取
$$
\widetilde V_0=(\ell,\ell w,\ell+T,\ell+T),
$$
$$
\widetilde V_1=(0,0,m-\ell\rho,m+\ell\rho)
=(0,0,-2c\rho,2b\rho).
\tag{2}
$$
它们满足
$$
\tau(\widetilde V_0)=\ell\lambda,\quad
\tau(\widetilde V_1)=0,\quad M=\ell^2\delta-m^2.
\tag{3}
$$
记
$$
\widetilde Z_0=N_4(\widetilde V_0),\quad
\widetilde Z_2=N_4(\widetilde V_1),\quad
\widetilde Z_1=N_4(\widetilde V_0+\widetilde V_1)
-\widetilde Z_0-\widetilde Z_2.
$$
则完整原恒等式为
$$
\boxed{
\begin{aligned}
\widetilde Z_0={}&
\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD\\
&+2\ell u w(\ell c_\lambda+T)\\
&+2\mathcal V(\ell^2+\ell c_\lambda T+T^2)
+2bc\,t(T^2-\ell^2).
\end{aligned}}
\tag{4}
$$
$$
\boxed{
\widetilde Z_1=
2(\ell c_\lambda+2T)(u\mathcal V-\ell\mathcal W)
-2\ell Mw+4bc\,mTt.
}
\tag{5}
$$
$$
\boxed{
\widetilde Z_2=
2\bigl((u^2-\ell^2Q)\mathcal V
-2m\ell\mathcal W-\ell Mf-bcMt\bigr).
}
\tag{6}
$$
这些是完整 N4、完整极化和完整 N4 的身份；没有取分量代替原条件。每式对 $A_1,f,\mathcal V,\mathcal W,t$ 至多一次，系数仅含权、lambda、T。

## 3. 推导与精确验证

把 (2) 代入 (1)，使用 (3)，按
$N_4(\widetilde V_0+\sigma\widetilde V_1)$ 的独立标量 sigma 收集0、1、2次系数即得 (4)–(6)。只涉及原迹、真 double-germ 乘法和同一个原 Gram 算子。

例如
$$
\tau(\widetilde V_1^2)=\ell M,\quad
\tau(d\widetilde V_1^2)=M(cX+bY),\quad
\tau(\widetilde V_1\mathcal K\widetilde V_1)=-2bcMt,
$$
$$
(u^2-\ell^2Q)\mathcal V-2m\ell\mathcal W=M(cX+bY).
$$
代入 (1) 立即给 (6)；交叉项给 (5)，常数项给 (4)。没有用均值方程约去误差，也没有倒 ell、rho、D、值首项或范数。

自含小源另外直接构造原四行和 (1)，在九自由变量的 BigInt 稀疏多项式环中实际核回所有9条身份；不从右式反定义 N4。

## 4. 与当前 W 相接

在当前已付 ell 的 W 原图，令 $V_i=\widetilde V_i/\ell$。
齐次性给 $\widetilde Z_i=\ell^2 Z_i$。沿[已刊原低 D 次压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，令
$$
K_{\rm val}=\ell^2(4\lambda^3-6\lambda^2+3\lambda-1)
-3\ell A_\lambda T+2T^3.
$$
完整低 D 次条件为
$$
V_{\rm low}=\ell^{-2}\left(
D\widetilde Z_0+\frac{K_{\rm val}}{2m}\widetilde Z_1+
\frac{D^2}{M}\widetilde Z_2\right).
\tag{7}
$$
(4)–(6) 在一般原 Gram 上成立；(7) 作为原值压缩的解释保留已刊 W、D 非零及已付 m、M 的范围，不向 h=k 或别的未付图外推排除。

本条不给新投影、排空或有限性改进。它给出更小的完整原输入；17703 原失败及待首次执行的缩放 V 源保持原字节。

## 5. 首次实际记录

[可读源](../notes/2026-11-28-unit211-general-scaled-entire-N4-three-compact-identities-8542.js)与[首次实际回执](../notes/2026-11-28-unit211-general-scaled-entire-N4-three-compact-identities-8542-execution.json)。

源 SHA256：
39b490ebb38cb807dc5a1401d2156561698d0d213e42ac5e065770cb31c2bf29；
4170 B。

本会话 V8 首次实际6毫秒，359次整数多项式乘法，9条完整身份差为零。三条实际原多项式项数145、29、28。无浮点、抽样或模提升，没有重跑旧原门。只保存小源、定义、SHA和小回执，无系数缓存。
