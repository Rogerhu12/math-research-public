# 从实际 Cartesian prefix-base 首 jet 直接给全角 G 界

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

这条短路由用于新真 CP 生成其自有 `prefix-base.json` 之后，直接检查
该**实际存储几何**的入口。它不把 R84 的 warm 值或 raw CP 值搬给新图，
也不需要等完整径向 target supplier 运行。

## 1. 有限表示与完整证明

当前 flat-profile 中心有 $a(0)=1$，冻结 chart 首值为1，所以目标材料角
在入口满足
$$
u=\psi-\frac w3\sin3\psi,\qquad
\rho=1-w\cos3\psi,\quad w=8q_{\rm ref},\quad0<w<1.
\tag{1}
$$
所有保存 binary 常数准确解释成 dyadic 数；不以精确 $1/10$ 代替
binary $q_{\rm ref}$。

定义 base 的首位置 jet 是一个完整有限 Cartesian Fourier 圈，写成
$$
F=R(\psi)e_r(\psi)+T(\psi)e_\theta(\psi)+Z(\psi)e_z,
$$
其中 $R=R_0+\sum R_j\cos3j\psi$、
$T=\sum T_j\sin3j\psi$、$Z=Z_0+\sum Z_j\cos3j\psi$。
这里是完整绝对位置系数，已包含圆背景；没有再加未截断的 $e_r(u)$。
令 $z=e^{3i\psi}$，定义
$$
\begin{aligned}
A&=\sum_j\tfrac12(3jR_j+T_j)(z^j-z^{-j}),\\
B&=R_0+\sum_j\tfrac12(R_j+3jT_j)(z^j+z^{-j}),\\
C&=\sum_j\tfrac12(3jZ_j)(z^j-z^{-j}).
\end{aligned}
$$
完整旋转基求导给 $F_\psi=(iA,B,iC)$，因此准确有限 Laurent 多项式
$$
H=-A^2+B^2-C^2-\rho^2
\tag{2}
$$
满足 $\Gamma=G/a^2-1=H/\rho^2$。
各系数均有理；均值高度的角导数自然消失。

采用 R84 的
$S_K=\sum_{k=0}^{K}(k+1)[(w/2)(z+z^{-1})]^k$ 及准确正尾
$$
T_K=\frac{w^{K+1}((K+2)-(K+1)w)}{(1-w)^2}.
$$
由该结果已经证明的 Fourier $\ell^1$ 乘法和正系数尾，直接得到
$$
\|\Gamma\|_\infty\le\|HS_K\|_{\mathcal A}
+\|H\|_{\mathcal A}T_K.
\tag{3}
$$
这次 $H$ 本身有限，不需要 R84 中对非多项式背景额外展开指数。
所以(3)是完全有限有理计算加一项显式无穷尾，覆盖全部角度。

## 2. 使用方式与对象范围

程序 `scripts/78718-geometry-base-inlet-angular-bound-v1.py` 的参数为
`--geometry <实际prefix-base.json> --out <新报告.json>`，默认 $K=96$。
它通过现有无损 storage reader 读取真正的
`payload['jets'][0,0,:]`，没有用来源 CP 的首点替代。
它只接受 defining base，核其初节点0、flat profile、ell0、chart首值1
与正确有限基布局。所有原输入保持不动。

输出包含准确连续上界、向上 $10^{-18}$ 网格值、两轴准确分数、原始
base/存储数据身份和 source CP 标识。全径向 target 仍按原流程生成；
本报告不代表全 prefix、最终 common map 或全曲面已经通过。
若后续 common-cut 在入口附近严格为零，且最终角向目标仍为(1)，其
入口转移可通过该真实对象关系证明；程序本身不默认为已经证明此关系。

原 `scripts/78718-geometry-inlet-angular-bound-v1.py` 也已接受任意符合
同一 flat/三重入口定义的新 CP；没有 warm SHA 硬限。两条路由对应不同
有限对象，应按实际需要使用自己的输入与报告。

## 3. 在已存在 M14 base 上的实际计算

真实 **3bdbb8 自然 exit0**，约2.039秒，读取已存在的
`notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json`
（Cartesian M24、来源 M14），得到
$$
\|\Gamma\|_\infty\le\frac{13311420728}{10^{18}}
=1.3311420728\cdot10^{-8}.
$$
其 $\psi=0$ 准确分数的近似为
$-1.3311420566797906\cdot10^{-8}$，另一轴约
$+5.0877930892845276\cdot10^{-11}$。与 raw CP 略有差别，程序没有把
这种表示差异抹掉。它没有改善旧图，也不替代已有 R81 的最终对象否决。

报告 `notes/2026-11-10-78718-geometry-m14-base-inlet-angular-bound-v1.json`，15249 B，SHA256
`72bf85c20b79722209f56253a6991b1a73cd9aa4fa7287809ca0424db511ed03`。
这是对实际首 jet 的新有限计算，0 BVP、0 tail、0几何修改。新的 M15 真输出
尚须由它自己的 base 执行此式，不能继承旧数值或 warm 的1.3024e−9。

