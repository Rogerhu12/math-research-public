# 完整独审：径向平均混合曲率守恒与正则有心帽必要条件

独立审查人：tail_review_continued_2，2026-11-10。
本审查未参与被审稿推导，已全文读取全部5节并核其引用实例的准确材料单位。
**接受全部必要条件及其明确范围，未发现阻断或需要作者勘误之处。**
没有运行数学程序、PDE、BVP、tail、RK或主轨迹。

## 1. 不可变来源与结论范围

被审稿：
[013eba46d6875cf0f6e83ce3fb66e430a9f1e05b](https://github.com/Rogerhu12/math-research/blob/013eba46d6875cf0f6e83ce3fb66e430a9f1e05b/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-radial-mixed-flux-cap-gate-v1.md)，
路径notes/2026-11-10-db6f-radial-mixed-flux-cap-gate-v1.md，
Git blob308f30f00c6d8c82b0471d84d5694d74e46c3e70，
6,088 UTF-8 B，
SHA-256 2581f2b01e1dfdd86cd7c11b8e18f031c5abc22e9a8074f2d85186ca1138eebe。
完整固定回读与字节哈希均已核同。

结论限定于整个桥保持同一个共同径向材料度量
g=dr^2+a(r)^2du^2，u周期ell、a>0，
并使用同一连续单位法向。
守恒量为J=a int_0^ell M du。
正则圆盘中心要求这个常数为零；
原直纹种子给非零值，新的单位速率柱核和实际有心帽给零值。

这是对这种径向有心帽接法的必要条件，
不是充分接合定理，也不是所有闭曲面、非径向中段或其他拓扑的不可能性。
主flat17的数据没有在本文读取或检验，不能把这些数值代入未知主候选。

## 2. Codazzi守恒的符号与C2正则度

设e_1=F_r、e_2=F_u/a。
从|F_r|=1、F_r·F_u=0、|F_u|=a，
直接求导得到

\[
F_{rr}=LN,\qquad F_{ru}=a'e_2+MN.
\]

Weingarten公式为
N_r=-Le_1-(M/a)e_2、N_u=-Me_1-(C/a)e_2。
因此对于光滑图，

\[
M_r-L_u
 =F_{ru}\cdot N_r-F_{rr}\cdot N_u
 =-\frac{a'}aM.
\]

第二项为零，第一项的唯一切向贡献是
a'e_2·[-(M/a)e_2]。
混合三阶导数相等后确实以此符号相消，没有遗漏a因子。

C2图也够用。
其二阶导数连续，N为C1；
二阶导数的弱导数是一阶分布，
与C1的N相乘及相应乘积公式可由C1测试函数的光滑逼近解释。
具体地，

\[
\partial_r(F_{ru}\cdot N)
 =(\partial_rF_{ru})\cdot N+F_{ru}\cdot N_r
\]

及对应u式在弱意义成立；
混合分布导数可交换，差式仍为上面的连续右端。
不需要假定C非零或第三阶经典导数存在。

a是径向C1系数，故

\[
(aM)_r=aL_u
\]

在分布意义成立。
周期积分消去右端，因为a不依赖u。
J连续且弱导数为零，于连通径向区间上就是普通常数。
实际C2贴合的接缝使a、M及同一法向连续，
因此这个常数会跨越拼接传递。

Gauss曲率的符号与C角零点都没有参与该证明。
增减曲率、穿过C=0或更换以其他系数为分母的局部表示，
本身不能改变同一径向几何的J。

## 3. 正则中心为何迫使J=0

真正C2正则圆盘中心附近，
形算子在实际光滑材料坐标中有界，记其范数界为K_0。
虽然极坐标u在中心退化，但在穿孔邻域
partial_r为单位切向、partial_u长度为a。
因此坐标混合系数满足

\[
|M|=|II(\partial_r,\partial_u)|\le K_0a.
\]

若这些材料圆周收缩到正则中心，a趋零，
从而

\[
|J|\le K_0\ell a^2\longrightarrow0.
\]

常数J只能为零。
因为a>0，整个穿孔径向桥上的int M du也为零。

这里没有要求先给出极坐标中心的所有形式展开；
实际C2正则性已经给所需的形算子有界。
反之，若端点是锥顶或其他非正则点，这个有界性未付，
就不能拿本节证明当作它已经正则。
零J只是一个必要条件，不推出圆心存在、空间闭合、两jet匹配或嵌入。

## 4. 原直纹值、共同材料单位与重标

已审原直纹族的实际公式可写为
F(v,u)=c(u)+v d(u)，u为球面单位弧长。
若T=d_u、n=d×T，则c_u=b n，
所以

\[
F_v=d,\quad F_u=b n+vT,\quad
a(v)=\sqrt{b^2+v^2}.
\]

按连续定向N=F_v×F_u/a，利用d×n=-T、d×T=n，
得N=(-bT+vn)/a。
因此M=F_vu·N=T·N=-b/a，
这独立核了原稿的符号和尺度。

这套公式同时适用于所引恢复版直纹环带和正C固定H版本；
后者改变球面曲线但保留球面弧长规范与c_u=b n结构。
其真实材料周期为ell，故

\[
J=a\int_0^\ell(-b/a)\,du=-b\ell\ne0.
\]

如果随后的正C截止或母线延拓确实保持同一个共同径向gauge，
第2节使其仍为此非零值。
所以不论中段曲率符号怎样，这一路不能通过这种径向中段
形成一个C2正则有心帽。
不含径向极点的闭合拓扑不在这项排除范围内。

若改用u=c theta、c=ell/(2pi)>0、theta周期2pi，
须同时变换度量系数和混合II：
a_theta=c a、M_theta=c M。
于是

\[
J_\theta
 =(ca)\int_0^{2\pi}cM(c\theta)\,d\theta
 =cJ=-\frac{b\ell^2}{2\pi}.
\]

不能只换积分上限而保留原a、M。
数值因规范而变，零与非零的判断不变。

引用的原数据来源为
[恢复直纹稿456c246b252e102e5a3d29c45b9d4dde7146dcea](https://github.com/Rogerhu12/math-research/blob/456c246b252e102e5a3d29c45b9d4dde7146dcea/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-geometry-explicit-ruled-saddle-annulus-recovered-v2.md)
及
[正C固定H稿ec5093a6d7c368dfaf80855d03c5c0f19ac51afe](https://github.com/Rogerhu12/math-research/blob/ec5093a6d7c368dfaf80855d03c5c0f19ac51afe/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-bump-fixed-h-v1.md)。
它们作为已审中间结论使用，本节另行核了实际单位变换。

## 5. 新柱核和实际帽确实过零门

单位速率平面曲线的圆柱F(r,u)=gamma(u)+r e_z具有
a=1和F_ru=0，所以M=0、J=0。
这适用于已完整独审的
[be7b380055c1906a1abacfc5682da0e372ef8579圆柱核](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)，
也适用于任何其他真实共同单位速率平面核。
升降Q领只要保持同一径向gauge，仍有零J。
这条一般计算不代替其他核心构造自己的闭合、幅度或嵌入证明。

实际有心帽
[b86b496d59518717e9335a098879c657395df899](https://github.com/Rogerhu12/math-research/blob/b86b496d59518717e9335a098879c657395df899/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-k-centered-cap-flat-outlet-v1.md)
的中心正则性已经另行全文独审，
报告固定在
[758407b0f63f61ef3250d3ed47352f11574038bb](https://github.com/Rogerhu12/math-research/blob/758407b0f63f61ef3250d3ed47352f11574038bb/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-positive-k-centered-cap-flat-outlet-v1.md)。
因此本报告第3节直接给帽的J=0。

原稿还有独立的公式核：
s(rho,u)在u反向时为偶函数，phi为奇函数；
s_rho、phi_u为偶，s_u、phi_rho为奇，
母面主曲率只依赖s，故相应II混合分量M为奇函数。
其完整2pi周期平均为零，与中心论证一致。
有限平坦外领再由守恒保持零J。

两端同为零只表明这个必要标量条件相容。
还没有匹配整个圆周的实际位置、框架、全部II、
径向斜率转折或共同材料度量的完整边值条件。

## 6. 换向、缩放与非径向源项

固定实际单位法向时，反转r或u都会使M变号；
整体反转法向也使M变号。
若按新参数重新选叉乘法向，某些符号变化相互抵消。
这些约定都不会改变零门。

空间乘lambda>0，并令新物理弧长径向R=lambda r，
则F_new(R,u)=lambda F(R/lambda,u)。
其混合导数F_new,Ru=F_ru，所以M_new=M；
而a_new=lambda a。
故J_new=lambda J，不能把非零值变成零。

非径向例子的计算也正确。
对于正交度量dr^2+a(r,u)^2du^2，
F_rr和F_ru的上述分解仍给第一Codazzi式
M_r=L_u-(a_r/a)M。
于是

\[
\frac d{dr}\int_0^\ell aM\,du
 =\int_0^\ell aL_u\,du
 =-\int_0^\ell a_uL\,du.
\]

右端通常不为零。
这说明原守恒证明的径向假设确实起作用，
而不是悄悄适用于任意正交材料度量。

单纯给同一径向几何改坐标名称不会使原来被追踪的非零通量消失；
只有实际延拓条件不再保持该径向Killing结构时，
才不能继续直接应用原来的J公式。
原稿没有声称已经构造这种非径向桥，
本报告也不把有源项公式当作桥的存在证明。

## 7. 实际证据和最终接受范围

来源绑定检查身份：
tail-review-radial-mixed-flux-binding-01。
clock实际返回2026-11-10 00:16:09 UTC；
JavaScript/V8只核完整6,088 B文本及SHA-256，
全部符合冻结来源。
没有符号程序、数值积分、PDE、BVP、tail、RK或几何数组执行。

全文接受：
径向J守恒、C2弱式正则度、正则中心零必要条件、
原直纹族的准确非零值及角重标、
新凸柱核与实际帽的零值、
方向/尺度变换和非径向有源项。

本报告不把J=0称为充分匹配，
不把原直纹的径向有心帽排除升级为一般闭面不可能，
也不对未读取的主flat17候选作判断。
仅新建本审稿，不改作者稿、HANDOFF、LOG或results。
