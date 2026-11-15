# R307：完整 self 的普适九次层、真实 history 系数与全母包消去

日期：2026-11-15。**完整纸面证明；没有执行新的符号展开程序、profile 求积、秩计算、人工检查或科学运行。**

[R303](R303-complete-self-degree-nine-and-all-translation-control.md) 已证明：固定非零实紧母包 u 后，全部完整 self 平移轮廓在 $\operatorname{Pol}_{\le9}$，且十条明确真实响应覆盖这个空间。本稿进一步消掉其中对母形的一个真实依赖：**最高九次层在所有母包上只有同一个几何系数**，乘以
$\int(u'')^2(u''')^2$。该系数有一个保真实累计 history 的明确原式，并由一条 pure-zero、九矩零响应准确支付。

因此，R303 若已把任意一个非零母包的全部中心 self 清零，就已经同时令所有其他母包的平移次数降至八。它仍不支付余下各层，不将它们默认成同一个 profile 能量。

## 1. 同一原查询与先前完整次数结论

采用 R297/R298 的全成本空间 U 线性观测
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0),
\qquad u_c(x)=u(x-c).
\tag{1}
$$
所有原函数使用同一右锚，紧 profiles 与两 collar 留正距离。允许中心 c 只在真实共同区间内变化；以下按有限多项式比较系数，不需要实际取 $c\to\infty$。

R303 已从完整 R56/R73 分子证明
$$
c\longmapsto\mathfrak q_{u_c}(V)\in\operatorname{Pol}_{\le9}
\quad(V\in U).
\tag{2}
$$
证明保留了完整左尾与移动积分下限。特别，对一个真实 $M_B=0$ 闭块，第二 history 是
$$
m(s)=\int_{s_0}^sM(t)\,dt,\qquad m(s_0)=m(s_1)=0,
\tag{3}
$$
而不是每个原语重新置零。

置
$$
m=m_{p_2},\qquad b=m_{p_1},\qquad t=m_{t_1},
\qquad d=h\omega-k,\qquad\gamma=h_s .
\tag{4}
$$
本稿的 t 是八矩累计坐标 $m_{t_1}$，不是 profile 坐标或射影流参数。点态 R73 身份为
$$
m_s=-kh/2,\qquad b_s=-kd.
\tag{5}
$$
$t_s=M_{t_1}(s)$ 始终是同一真实八矩密度，包含其原局部导数项，不另作独立几何参数。

## 2. 完整二阶分子的两个最高系数

在平移后的母包坐标 $y=x-c$ 中记
$$
v=u'(y),\qquad r=u''(y),\qquad r'=u'''(y),
$$
$$
J_0(y)=\int_y^{r_*-c}r(\eta)^2d\eta,\qquad
J_1(y)=\int_y^{r_*-c}\eta r(\eta)^2d\eta .
$$
共同右零 collar 支付移动锚；所有 J 始终来自同一个 u。

由 R255/R73 完整八矩式，
$$
[c^4]W_2=-\frac m4J_0.
\tag{6}
$$
为了读九次 self，必须再保完整三次项。只有 $p_2,p_1,t_1$ 三个原坐标贡献这一层，准确为
$$
\boxed{
[c^3]W_2
=-\frac m2\{v^2+yJ_0+J_1\}
+\left(t-\frac b4\right)J_0 .
}
\tag{7}
$$
其中 $v^2$ 是 $p_2$ 的原局部项，不能只保右积分。

R295 的完整局部恢复项
$$
\eta_0=
-\frac{e_s(1+e^2)}{16h^2}r^2+
\frac{\gamma(1+e^2)}{8h^2}vr
-\frac{\gamma e}{8h}v^2-\frac1{16}\partial_s(J_e/h)
$$
给
$$
[c^3]\eta_0=-\gamma r^2/16.
\tag{8}
$$
这里 $e=h(y+c)+d$；$\partial_s(J_e/h)$ 至多二次，未被删除。

令
$$
A_Z=(W_2)_x/2+\eta_0/h,\qquad
V_Z=(A_Z,zP+B,eA_Z-hW_2).
$$
从(6)–(8)得到
$$
[c^4]A_Z=mr^2/8,
$$
$$
[c^3]A_Z
=-\frac m2vr-\frac m4J_0+\frac m2yr^2
-\frac12\left(t-\frac b4\right)r^2
-\frac{\gamma}{16h}r^2.
\tag{9}
$$
用 $J_0'=-r^2$、$J_1'=-yr^2$ 逐项微分，
$$
[c^3](A_Z)_x
=\frac m4r^2-\frac m2vr'
+\left(my-t+\frac b4-\frac{\gamma}{8h}\right)rr'.
\tag{10}
$$

完整第三分子的导数是
$$
(V_Z)_{{\rm third},x}
=e(A_Z)_x-\frac h2(W_2)_x+\eta_0.
\tag{11}
$$
因此，置
$$
L=\frac{dm}{4}-ht+\frac{hb}{4}-\frac{\gamma}{8},
\tag{12}
$$
其两个最高平移系数准确为
$$
\boxed{
[c^5](V_Z)_{{\rm third},x}
=\frac{hm}{4}rr',
}
\tag{13}
$$
$$
\boxed{
[c^4](V_Z)_{{\rm third},x}
=\frac{hm}{8}r^2-\frac{hm}{2}vr'
+\left(\frac54hmy+L\right)rr'.
}
\tag{14}
$$
另外两个分量的次数分别至多四、三，所以它们的平方不贡献九次项。本节不是只抽最高 profile jet；(7)、(8)、(14)保留这一平移层所需全部低 jet/局部/原尾来源。

## 3. 完整能量配对，未删低阶尾

定义三条真实母包积分
$$
\mathcal I(u)=\int r^2(r')^2,\quad
\mathcal J(u)=\int vr(r')^2,\quad
\mathcal I_1(u)=\int y\,r^2(r')^2.
\tag{15}
$$
不假定后两条为零。

由(13)、(14)，完整 $E_Z=\int|V_{Z,x}|^2$ 的九次项为
$$
\boxed{
[c^9]E_Z
=-\frac{h^2m^2}{4}\mathcal J
+\frac{5h^2m^2}{8}\mathcal I_1
+\frac{hmL}{2}\mathcal I .
}
\tag{16}
$$
唯一另一个乘积是 $h^2m^2\int r^3r'/16$，其真实紧支边项为零。

R303 已明确把固定左 collar 到移动包左端的积分分开：
$$
E_Z=(a+c-\ell)|U_c|^2+
\int_a^b|V_{Z,x}(s,y+c)|^2dy.
$$
$U_c$ 至多二次，所以第一项至多五次。R295 完整 period 公式中的其余外尾
$U_c\cdot V_c,|\nabla_sU_c|^2,|U_c|^2$
至多四次。因此它们没有九次贡献；这里没有把原二阶场误认成紧支撑场。

R295 的正 $H(Z,Z)$ 左二次系数含 $kE_Z/(2h)$，而(1)在 $\phi=0$ 给其 $-1/4$。于是
$$
[c^9]\mathfrak q_{u_c}(V_B)
=\frac{\mathcal J}{32}\int khm^2ds
-\frac{5\mathcal I_1}{64}\int khm^2ds
-\frac{\mathcal I}{16}\int kmL\,ds.
\tag{17}
$$
真实 $M=0$ 与(5)使
$$
\int khm^2ds=-\frac23[m^3]_{s_0}^{s_1}=0.
$$
因此前两项的消失来自几何原端值，**不是**把 $\mathcal J$ 或 $\mathcal I_1$ 假设为零。

## 4. 一个所有母包共有的真实 history 系数

从(12)、(17)先得到
$$
[c^9]\mathfrak q_{u_c}(V_B)
=\mathcal D_9(B)\,\mathcal I(u),\qquad
\mathcal D_9(B)=-\frac1{16}\int kmL\,ds.
\tag{18}
$$

其中含 $d m^2$ 和 $b m$ 的两项还会准确相消。由(3)、(5)，
$$
\int kdm^2ds
=-\int b_s m^2ds
=2\int bmm_sds
=-\int khbm\,ds.
\tag{19}
$$
代入(12)、(18)，得到完整可消费的原式
$$
\boxed{
\mathcal D_9(B)=
\frac1{16}\int_B kh\,m_{p_2}m_{t_1}\,ds
+\frac1{128}\int_B k h_s\,m_{p_2}\,ds.
}
\tag{20}
$$
全部 m 是同一个原始累计八矩，第二项的 $h_s$ 原 chain 贡献保留。若删掉(8)会漏掉这个项。

也可用 $m_s=-kh/2$ 对第一项再分部积分：
$$
\boxed{
\mathcal D_9(B)=
\frac1{16}\int_B m_{p_2}^{\,2}M_{t_1}\,ds
+\frac1{128}\int_B k h_s\,m_{p_2}\,ds.
}
\tag{21}
$$
两式相等只用同一双端 m=0；不把 $M_{t_1}$ 当作可任意独立指定的新输入。

所以
$$
\boxed{
[c^9]\mathfrak q_{u_c}(V_B)
=\mathcal D_9(B)
\int (u'')^2(u''')^2
\quad\text{对全部真实紧母包 }u.
}
\tag{22}
$$
这已包含该层的全部 $C^2$ 余项；第 2–3 节直接从完整分子和完整 period 读取，没有在主符号后补猜余项。

## 5. 全 U 的真实线性泛函与普适兼容

式(20)对几何原变量含二次 history，并不意味着这些几何变量线性独立。它的**成本函数**定义则准确线性。

固定任意非零实紧 $u_*$，令
$$
\boxed{
\mathcal D_9(V)=
\frac{[c^9]\mathfrak q_{(u_*)_c}(V)}
{\mathcal I(u_*)},
\qquad V\in U.
}
\tag{23}
$$
R303 给有限九次次数上界，所以分子可由十个真实允许中心的查询经固定 Vandermonde 逆提取。分母严格正；(23)是有限个原 profile/输出查询的准确线性组合。

对每个真实生成成本，(22)表明此定义与 $u_*$ 的选择无关，并等于(20)。线性延拓至 U 得
$$
\boxed{
[c^9]\mathfrak q_{u_c}(V)
=\mathcal D_9(V)\mathcal I(u)
\quad(V\in U,\ u\text{ 为任意真实紧母包}).
}
\tag{24}
$$
因此不同母形最高 self 层之间有一个完整原身份：
$$
\mathcal I(v)[c^9]\mathfrak q_{u_c}(V)
-\mathcal I(u)[c^9]\mathfrak q_{v_c}(V)=0.
\tag{25}
$$
这不是只对 same $\mathcal F^\star$ 母包成立；它对任意两条真实紧输入成立。相反，它不使其余八层也只依赖同一 $\mathcal I$。

式(24)精确说明：全母包完整 self 的最高平移层是一维。它不声称整个 self 函数空间、整个成本 U 或整个正字符空间是一维。

## 6. 一条准确 pure-zero、九矩零的普适消去方向

R303 已付真实响应
$$
\mathcal K_{\rm top}=\mathcal B_{p_2}(\mathfrak H_6),
$$
以及
$$
\pi\mathcal K_{\rm top}=0,\qquad
\mathsf T(\mathcal K_{\rm top})=0,\qquad
[c^9]\mathfrak q_{u_c}(\mathcal K_{\rm top})
=-1080\,\mathcal I(u).
\tag{26}
$$
其原 finite-flow 及 N 链证明保所有右常数；这里不重算。

规范化
$$
R_9=-\mathcal K_{\rm top}/1080.
$$
则
$$
\boxed{
\pi R_9=0,\qquad \mathsf T(R_9)=0,\qquad
\mathcal D_9(R_9)=1.
}
\tag{27}
$$
给任意 $V\in U$，置
$$
\widehat V=V-\mathcal D_9(V)R_9.
\tag{28}
$$
这是完整真实函数空间中的有限原响应修正，且
$$
\pi\widehat V=\pi V,\qquad
\mathsf T(\widehat V)=\mathsf T(V),
$$
$$
\boxed{
c\longmapsto\mathfrak q_{u_c}(\widehat V)
\in\operatorname{Pol}_{\le8}
\quad\text{对所有真实紧母包 }u.
}
\tag{29}
$$
(28)先是响应线性空间的结论，不将一个负实系数直接当作负路径。

若要真正安装该有限观测，R297 的九条矩阵单位可各减去其 $\mathcal D_9$ 值乘 $R_9$。九条修正列加 $R_9$ 给
$$
(\mathsf T,\mathcal D_9)(\mathcal R_{\mathrm p0})
=\operatorname{Mat}_3(\mathbb R)\oplus\mathbb R.
\tag{30}
$$
R222 的一般有限观测定理因此可与 whole pure 同时支付(30)，保全部 prototype 基准、真实桥、full-pure 校正的 mixed 成本以及最后有限复制。再按原 Klein 四块可得到真实闭 hook，满足
$$
M=0,\quad \mathbf T=\kappa\mathfrak H,\quad
\pi V=0,\quad \mathsf T(V)=A,\quad\mathcal D_9(V)=d
\tag{31}
$$
的任意指定有限目标。特别 $A=0,d=0$ 是真实可实现的条件；没有通过倒行把成本符号翻转。

本稿不单凭(30)另宣保持预先冻结的 Gaussian germ、度量或其他已定观测。若调用 R302 的原词结构及增强 IFT，应把这些实际需要的有限观测从起点纳入同一联合系统。

## 7. 对 R303 已构造几何的一个无需新控制的推论

若某个实际 $V$ 已通过 R303 支付一个非零母包 $u_0$ 的**整个**平移 self，
$$
\mathfrak q_{(u_0)_c}(V)\equiv0,
$$
则由(24)与 $\mathcal I(u_0)>0$，
$$
\mathcal D_9(V)=0.
$$
所以同一个实际 V 已经满足
$$
\boxed{
\mathfrak q_{u_c}(V)\in\operatorname{Pol}_{\le8}
\quad\text{对所有其他母包 }u.
}
\tag{32}
$$
这个推论不需要再安装 $R_9$，也不改变那条实际几何。它正是从同母结论得到的一个真正全母接口。

但(32)只降次数。它没有令新的八次多项式为零，没有给多个不同母包的余下完整 self 联合秩，也没有证明全部
$u\mapsto\mathfrak q_u(V)$
可由现有响应共同消去。

## 8. 后继任务的准确起点

本稿已经支付全 Q 的最高平移层：完整原式、所有母形的共同系数、明确 pure/矩阵核响应以及真实有限安装均齐全。

下一问题是 $\ker\mathcal D_9$ 上的完整八次层及以下各层。它们可能含更多独立的真实母包泛函和完整 $C^2$ 余项；不能把(24)的一个 $\mathcal I$ 延伸为未经证明的全层公式。任何新增原式消费者都应只处理真正尚未付的层，复用已发表局部 A、完整八矩二次式及真实尾，不重旧 canonical forcing、八 χ 或既有 pure 分类。

本稿未支付 R225 的全部平台仿射、通量、内部退化、端 germ 或同一二阶 gauge 的完整 ruling。所有“消去”均按所写的准确最高层范围理解。

作者责任：以上新推导全部为有限手写原式微分、同锚分部积分及已付真实控制定理的应用；没有新增科学执行，也没有用形式独立尾值代替真实输入。
