# R271 附录：倒数第二出生固定块的双复制正矩与内部相邻一致上界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：已证明；Astra-ISP-1cf8c51d 核对真实最小逆、双复制 Gram、全部 Gamma 因子与范围。

本稿给任意多个独立异权头的一个真实非交换相邻上界。范围严格为相对出生 $q-1$ 的整个 $q$ 维池固定 primitive 块，并且相邻的三个阶都必须是内部阶。它没有闭合零阶或最高阶相邻端点，也没有把这个约化块当作完整出生层。

## 1. 模型、源坐标和主结论

取
$$
q\ge2,\quad L\ge q,\quad a_i>0,\quad z_i=a_i^2,
\qquad
D=\sum_{i=1}^q a_iE_i+D_{\rm w},
$$
其中弱池有 $L$ 个权为一的物理位。固定
$$
s=q-1,\qquad h=L-q+2.
$$
使用 [R239 倒数第二出生块](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) 的真实源映射 $\mathcal E:\mathbb C^q\to K_s$，并仍先在完整物理层取逆：
$$
F_j=\frac{D^j(D^*)^j|_{\mathcal H_s}}{(j!)^2},
\qquad
H_j=\mathcal E^*F_j^{-1}\mathcal E,\qquad 0\le j\le h.
\tag{1.1}
$$
源坐标不预设正交；对应 primitive 压缩 $\Gamma_j$ 的实际坐标是 $H_0^{-1}H_j$。因此相邻算子序准确等价于同一个 Gram form 的
$$
\Gamma_j\Gamma_{j+1}^{-1}\Gamma_j\le C\Gamma_{j-1}
\quad\Longleftrightarrow\quad
H_jH_{j+1}^{-1}H_j\le C H_{j-1}.
\tag{1.2}
$$

**定理。** 对每个
$$
2\le n\le h-2,\qquad d=h-n\ge2,
$$
都有
$$
\boxed{
H_nH_{n+1}^{-1}H_n
\le
\frac{nd}{(n-1)(d-1)}
\frac{P(n-1)P(n+1)}{P(n)^2}\,H_{n-1}
\le
\frac{nd}{(n-1)(d-1)}H_{n-1}
\le4H_{n-1}.
}
\tag{1.3}
$$
这里真实标量多项式为
$$
P(x)=\sum_{R\subseteq[q]}z_R(x)_{|R|}(h-x)_{q-|R|},
\tag{1.4}
$$
上升阶乘的约定同上述 R239 稿。

所以这一整个固定块的内部比较常数不依赖头数、出生数、池大小或异权比例。若 $h<4$，范围为空，不能由本稿补出端点。

## 2. 保真实最小逆的矩阵测度

对头子集 $R$，令
$$
v_R=\left(\frac{1_{i\in R}}{a_i}\right)_{i=1}^q,
\qquad
d\nu(t,R)
=(L+1)\frac{z_Rt^{|R|}}{(1+t)^{L+2}}\,dt.
\tag{2.1}
$$
这是正的有限联合测度：其质量恰是第一个内部阶的标量分母。对所有 $1\le j<h$，
$$
\omega_{j,R}:=\int_0^\infty t^{j-1}\,d\nu(t,R)
=\frac{z_R}{\binom L{j+|R|-1}}.
\tag{2.2}
$$
原一参数最小逆因而准确写成
$$
H_j=A_j-\frac{b_jb_j^*}{M_j},
\quad
A_j=\int t^{j-1}v_Rv_R^*\,d\nu,
\quad
b_j=\int t^{j-1}v_R\,d\nu,
\quad
M_j=\int t^{j-1}\,d\nu.
\tag{2.3}
$$
所有量有限且 $H_j>0$。这里不是提出一个替代原最小逆的积分模型，而是原 R239 公式逐项的 Beta 积分。

## 3. 双复制使乘上质量后的 Schur 矩阵成为正矩

取两个独立副本 $(t,R)$、$(u,S)$。展开差向量的平方，准确得到
$$
\boxed{
J_j:=M_jH_j
=
\frac12\iint
(tu)^{j-1}(v_R-v_S)(v_R-v_S)^*
\,d\nu(t,R)\,d\nu(u,S).
}
\tag{3.1}
$$
两对角项各贡献 $M_jA_j$，两交叉项合并为 $2b_jb_j^*$，所以所有因子和系数都固定。

因此，对于相邻三个内部阶，
$$
\boxed{
\begin{pmatrix}
J_{n-1}&J_n\\
J_n&J_{n+1}
\end{pmatrix}\ge0.
}
\tag{3.2}
$$
这是一个直接积分的正 Gram：其被积列可取
$$
(tu)^{(n-2)/2}
\begin{pmatrix}
v_R-v_S\\
tu(v_R-v_S)
\end{pmatrix}.
$$
所需积分有限正是因为 $n-1,n,n+1$ 都属于 $1,\ldots,h-1$。

对严格正的 $J_{n+1}$ 取 Schur 补，由 (3.2) 得
$$
J_nJ_{n+1}^{-1}J_n\le J_{n-1}.
$$
还原 $J_j=M_jH_j$，得到一般的质量比预算
$$
\boxed{
H_nH_{n+1}^{-1}H_n
\le
\frac{M_{n-1}M_{n+1}}{M_n^2}\,H_{n-1}.
}
\tag{3.3}
$$
这一步适用于任意正联合测度的这种标量参数 Schur 方差。它没有错误宣称 $H_j$ 本身就是正矩，也没有省略质量比。

## 4. 真实 Beta 分母把质量比一致压到四

对当前模型，逐项 Gamma 公式给
$$
M_j
=\frac{\Gamma(j)\Gamma(h-j)}{\Gamma(L+1)}P(j).
\tag{4.1}
$$
[R239 倒数第二出生块 §8](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md#8-任意头归一化多项式的全部外实根与倒数正矩) 已证明：所有非恒定因子的根都为单实根，位于 $(-\infty,0)$ 或 $(h,\infty)$。单位头参数只贡献正的常数因子。本稿直接引用这个已发表结果，不重新登记分母实根结论，也不需要额外的根间隔性质。

这里只需要这些根的位置。若根记为 $\rho$，则
$$
\frac{P(n-1)P(n+1)}{P(n)^2}
=
\prod_\rho
\left(1-\frac1{(n-\rho)^2}\right)
\le1.
\tag{4.2}
$$
每个因子严格为正：$n,d\ge2$，而每个根均在上述两侧。没有根时乘积为一。

从 (4.1) 直接得到
$$
\frac{M_{n-1}M_{n+1}}{M_n^2}
=
\frac{n}{n-1}\frac{d}{d-1}
\frac{P(n-1)P(n+1)}{P(n)^2}.
\tag{4.3}
$$
因为两个整数 $n,d$ 均至少为二，(4.3) 至多为四。结合 (3.3) 即完成 (1.3) 的全部证明。

## 5. 第一下降语言与未付端点

按原正交高度定义的第一下降块，令 $\ell=n+1$。在本固定 primitive 链中，(1.2) 的系数 $C$ 对应
$$
A_{\ell+1}A_{\ell+1}^*
\le
C\left(\frac{\ell}{\ell-1}\right)^2
A_\ell^*A_\ell.
$$
所以本稿实际给
$$
\boxed{
A_{\ell+1}A_{\ell+1}^*
\le
\frac{(n+1)^2d}{n(n-1)(d-1)}
A_\ell^*A_\ell
\le9A_\ell^*A_\ell,
\quad
n=\ell-1\ge2,\ d=h-n\ge2.
}
\tag{5.1}
$$
这里所有相邻块仍属于同一真实源的正交链，不把环境 $D^*$ 替代受限伴随。

两个端点 $n=1$ 和 $n=h-1$ 没有被本稿支付。原最小逆在那里有限，但辅助质量 $M_0$ 或 $M_h$ 发散，故不能把它们代入 (3.3)。尤其本稿不证明通常最关键的高度二比较。

[三异权全出生稿](R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md) 已用有限精确证书付清三个头的全部端点；本稿新扩大的是任意头数时的上述内部范围，不重计那一已完成族。

一般全 primitive 空间、任意有限权型、原连续尾与真实窄 Schur 返回源的比较仍未由此自动关闭。
