# R54：共同径向度量的混合曲率通量与正则帽必要条件

**状态：已证明，完整未参与者独立审查通过。** 2026-11-10 UTC。
作者：独立几何分工；独立审查：tail_review_continued_2；root 已全文读作者与完整审稿后采纳。

对实际 C² 浸入和同一共同径向度量，J=a∮Mdu 守恒；真正 C² 正则圆盘中心强迫 J=0。
分布 Codazzi、真实周期和单位变换已完整核实，不要求 C 非零或曲率同号。
原指定直纹族 J=-bℓ≠0，故不能沿保持该径向 gauge 的任意中段补成正则有心帽；
新凸柱核和 R53 真实帽均通过 J=0 必要门。
这不是非径向桥或一般闭曲面不可能性，也没有检查或否定 flat17 主数值问题。
0 新数学程序执行；审者00:16:09 UTC只做来源文本核。

## 采用与来源锁

- 作者固定 commit 013eba46d6875cf0f6e83ce3fb66e430a9f1e05b，blob 308f30f00c6d8c82b0471d84d5694d74e46c3e70，6088 UTF-8 B；
  SHA256 2581f2b01e1dfdd86cd7c11b8e18f031c5abc22e9a8074f2d85186ca1138eebe。
- [完整独立审查](https://github.com/Rogerhu12/math-research/blob/6c123d0a9250e548666d60a0683a26d020b16b10/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-tail-review-radial-mixed-flux-cap-gate-v1.md)：
  commit 6c123d0a9250e548666d60a0683a26d020b16b10，blob 1080ff108133adfd3a91aedf122ef4be86f1fc8b，9229 UTF-8 B；
  SHA256 6bdb2bc03bcd6941525be0f28bd3d416c50e015141b33c2fa57e345bd512cfc1。
- 全文接受，没有数学阻断或待修勘误；不是只核有限常数或只审摘要。
- 本题 README 的闭曲面、G5、全图定量几何、新网格和最终未参与者完整重跑仍须各自支付。

下方逐字保留作者正文；原稿历史待审状态由本采用记录更新。

---

## 1. 精确守恒式

设一个实际定向C2等距浸入在圆柱材料域上诱导

$$
g=dr^2+a(r)^2du^2,\qquad u\in\mathbb R/\ell\mathbb Z,\qquad a>0 .
\tag{1}
$$

相对于同一个连续单位法向，记
L=F_rr·N、M=F_ru·N、C=F_uu·N。
则

$$
M_r=L_u-\frac{a'}aM,\qquad
\boxed{\quad J(r):=a(r)\int_0^\ell M(r,u)\,du
\text{ 与 }r\text{ 无关}.\quad}
\tag{2}
$$

证明不需要C非零，也不需要K保持某个符号。
直接由Gauss及Weingarten公式，

$$
F_{rr}=LN,\quad F_{ru}=a'e_2+MN,\quad
N_r=-Le_1-(M/a)e_2,\quad N_u=-Me_1-(C/a)e_2.
$$

交换混合三阶导数后，

$$
M_r-L_u=F_{ru}\cdot N_r-F_{rr}\cdot N_u=-(a'/a)M .
$$

对C3图这是逐点等式；对C2图，同一计算在分布意义成立：
二阶导数连续、N为C1，混合分布导数可交换；
乘积公式可用C1测试函数的光滑逼近核实。
因而(aM)_r=aL_u也在分布意义成立。
u周期积分给J'=0；J连续，故它是通常意义的常数。

所以经过任何保持(1)且位置/两jet实际贴合的中段，
同一J都会传递；正负曲率交替或C角零点不改变这个结论。

## 2. 正则有心帽必须使这个常数为零

假设同一径向gauge延到一个真正C2正则圆盘中心，
其材料圆周收缩到一点，a(r)趋0。
中心附近的实际形算子有界，设其范数最多K_0。
因为|partial_r|=1、|partial_u|=a，

$$
|M|=|II(\partial_r,\partial_u)|\le K_0a .
$$

于是

$$
|J(r)|\le K_0\ell\,a(r)^2\longrightarrow0 .
\tag{3}
$$

守恒(2)遂给

$$
J=0,\qquad \int_0^\ell M\,du=0
\quad\text{在整个同一径向桥上}.
\tag{4}
$$

这只是一条必要条件。零J没有证明帽的存在、
终端位置闭合、全部两jet或空间嵌入。
证明只用了a趋0和中心C2正则；没有把一个锥顶当成正则中心。

## 3. 原直纹族的实际单位与非零值

精确来源是
[原环带恢复正文456c246b252e102e5a3d29c45b9d4dde7146dcea](https://github.com/Rogerhu12/math-research/blob/456c246b252e102e5a3d29c45b9d4dde7146dcea/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-geometry-explicit-ruled-saddle-annulus-recovered-v2.md)，
及
[正C固定H版本ec5093a6d7c368dfaf80855d03c5c0f19ac51afe](https://github.com/Rogerhu12/math-research/blob/ec5093a6d7c368dfaf80855d03c5c0f19ac51afe/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-bump-fixed-h-v1.md)。

两类种子均取球面弧长u，真实周期为ell；
径向单位速率坐标是v，固定尺度为b>0。其实际公式是

$$
a(v)=\sqrt{b^2+v^2},\qquad
M(v,u)=-\frac b{\sqrt{b^2+v^2}}.
\tag{5}
$$

因此在这个精确gauge下

$$
J=a\int_0^\ell M\,du=-b\ell\ne0 .
\tag{6}
$$

后续正C截止或母线平坦延拓只要保持同一共同径向度量，
也保持(6)。所以这一个原直纹族不能通过任意这样的径向中段
直接补成正则有心帽。
这里不是说所有闭合方式都失败，也没有排除不含径向极点的拓扑。

若改用2pi周期角theta、u=c theta、c=ell/(2pi)>0，
必须同时改写

$$
a_\theta=c\,a,\qquad M_\theta=c\,M,\qquad
J_\theta=c\,J=-\frac{b\ell^2}{2\pi}.
\tag{7}
$$

不能只把积分上限从ell改成2pi而保持(5)的所有系数不变。
无论哪种规范，零与非零结论相同。

## 4. 新凸柱核和实际正K帽通过这一门

新核来源为
[be7b380055c1906a1abacfc5682da0e372ef8579](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)，
其共同单位速率材料角周期2pi，圆柱初始a=1、M=0，
所以J=0。任何后来保持这个gauge的升降Q延拓仍有J=0。
其他实际单位速率平面凸核gamma_t(u)+r e_z同样如此，
包括支持函数构造；此结论不替代它们自身的其他证明。

有心帽来源为
[b86b496d59518717e9335a098879c657395df899](https://github.com/Rogerhu12/math-research/blob/b86b496d59518717e9335a098879c657395df899/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-k-centered-cap-flat-outlet-v1.md)。
它的中心真实正则、a=sin rho、周期2pi，故(4)适用。
还有独立的直接核对：该稿(13)中s_rho、phi_u为u的偶函数，
s_u、phi_rho为奇函数；两个主曲率只依s，
在u->-u下不变。因此(15)给M(-u)=-M(u)，其平均为0。
帽的有限平坦外领依(2)也保持零J。

因此新凸柱核与这个真实帽至少通过同一必要零门。
完整函数边值匹配、径向转折及实际位置/两jet仍没有解决；
不能把共同零平均升级成充分接合条件。

## 5. 换向、缩放和适用范围

固定几何单位法向时，r或u的方向反转使M变号，
整体法向反转也使M变号。
若同时按参数方向重新选叉乘法向，符号会相应抵消。
这些约定最多改变J的符号，不改变零门。
正的常数角重标按(7)只乘正因子。

若空间整体乘lambda>0并把物理弧长径向坐标改为R=lambda r，
则a变为lambda a，混合分量M不变，J变为lambda J。
所以尺度变化也不能把(6)变成0。

本稿要求整个所讨论的桥使用(1)的同一个径向Killing材料gauge。
任意新的非径向坐标或非径向度量不能凭空沿用J守恒。
例如即使仍用正交形式dr^2+a(r,u)^2du^2，
相同第一Codazzi式只给

$$
\frac d{dr}\int_0^\ell aM\,du
=\int_0^\ell aL_u\,du
=-\int_0^\ell a_uL\,du ,
\tag{8}
$$

右端一般不为0。
(8)说明去掉径向假设后为什么当前证明不再适用；
它不是一个已构造的非径向桥。

当前主flat17没有在本稿中读取或核查这项通量，
不把任何上述符号或常数套到主数值候选。
本稿没有新的数学程序执行声明，须另付全文独审。
