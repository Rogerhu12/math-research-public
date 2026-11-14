# R95. 原完整 theta 的真实 p 同源分解与全部 norm carry

## 结论

对奇次数同源 \(\varphi:E\to E'\)、\(\varphi^*\omega'=c_\varphi\omega\)，
两端使用 reduced theta，则
\[
\psi_\varphi(z)=\frac{\theta_{E'}(c_\varphi z)}{\theta_E(z)^{\deg\varphi}}
\]
是准确规范的核有理函数。它的二次补偿为
\[
c_\varphi^2s_2(E')-(\deg\varphi)s_2(E)
=\sum_{0\ne Q\in\ker\varphi}\wp_E(Q).
\]
目标邻点一般不是方格；这项不可删去。

对真实 degree-\(p\) 邻点，原完整
\(U_P=Z(w)\Theta_P(z,w)\) 满足
\[
U'_{\varphi P}(\varphi z,\varphi w)=U_P^pD_{\varphi,P},
\quad
D_{\varphi,P}=
\frac{Z'(\varphi w)}{Z(w)^p\psi_\varphi(w)}
\frac{\psi_\varphi(P+z+w)}{\psi_\varphi(P+z)}.
\]
在共同次数 \(p+1\) 驯扩域中，
\(D_{\varphi,P},D_{\varphi,T}\in1+\mathfrak m\mathcal O[[Z_1,Z_2]]\)。
这一输入对正式对数只普遍保证
\(\log D_{\varphi,P}\in\varpi^{-1}\mathcal O[[Z_1,Z_2]]\)；
第 \(p\) 次对数项可以付出这一层分母，不能写成逐枝可除 \(p\)。

全部 \(p+1\) 个真实邻点却满足完整的准确乘积：
\[
\prod_G D_{\varphi_G,P}=D_{[-p],P},\qquad
\prod_G U^{E/G}_{\varphi_GP}(\varphi_Gz,\varphi_Gw)
=U_P^pU_{-pP}(-pz,-pw).
\]
\(\prod_Gc_G/p\) 在核函数与 \(Z\) 的乘积中准确相消。
任一单枝与负对偶还满足
\[
D_{[-p],P}=D_{\varphi,P}^{p}
  (\varphi\times\varphi)^*D_{-\widehat\varphi,\varphi P}.
\]
这准确复原 R92 的 \(1+p\) 平方修正，保留中间二次补偿和公共参考，
且无需在分歧域另假设 canonical Witt Frobenius。

## 原 256 标签的和

设 \(\mathcal R_P=\Theta_P/\Theta_T\)、
\(\mathcal A=\sum_P\mathcal R_P\)，\(C_{\varphi,P}=D_{\varphi,P}/D_{\varphi,T}\)。
则
\[
\mathcal A_\varphi\circ(\varphi\times\varphi)
=\mathcal A^p+
 \sum_P\mathcal R_P^p(C_{\varphi,P}-1)
-p\,\mathfrak C_p((\mathcal R_P)_P),
\]
其中
\(\mathfrak C_p(X)=((\sum X)^p-\sum X^p)/p\) 为整交叉多项式。
中间项只知在分歧极大理想中；合成负对偶或全部 norm 后
才能使用平方 Frobenius 的准确整格。

原 \(E_{17}\) 到 Legendre 中心的坐标换元给
\(U_{\rm Leg}(az,aw)=(1+\sqrt{17}/x_E(w))U_E(z,w)\)；
原参考二挠点变成 Legendre 的 \((1/2,0)\)。
这个固定 gauge 及参考点也已保留。

## 全文与用途

[完整证明](../notes/2026-11-12-geometric-p-step-theta-and-ramified-witt-carry.md)
由 reduced-theta 变换律、全部除子和首项逐式核定，
根端全文独审通过。来源包括 Bannai–Kobayashi 的原 theta 规范
及已经证明的实际 CM 邻点模型。

这些恒等式完整接合真实几何同源、原双变量 theta 与 Witt 层。
它们仍须经过原公共参考和指定对角的中央配对；
非零 norm 对数本身不等于目标中央导数非零。
