# R309：完整 self 的普适八次层、第二真实补偿与全母次数降至七

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、秩计算、人工检查或科学运行。**

[R307](R307-universal-degree-nine-self-layer-and-real-elimination.md) 已证明完整 self 的最高平移层在所有母包上等于同一个真实几何系数 $\mathcal D_9$ 乘 $\int(u'')^2(u''')^2$。本稿再保留原二阶分子的下一整层，得到准确八次系数：
$$
[c^8]\mathfrak q_{u_c}(V)
=\mathcal D_8(V)\mathcal I(u)
+\mathcal D_9(V)\{9\mathcal I_1(u)-3\mathcal J(u)\}.
$$
全部低阶局部项、原右尾与外平台边项按其真实次数处理，没有由主符号推断完整公式。

因此在 $\mathcal D_9=0$ 后，八次层也是一个所有母包共有的真实标量，且有明确 pure-zero、九矩零补偿。R303 已清任意一个非零母包全部平移的同一实际几何，事实上已使所有其他母包的完整平移次数降至七。

本稿只支付所写两层。它不使完整 self 函数为零，不解决完整 period/ruling，不把有限观测增控当作某个另有障碍的圆类已可实现。

## 1. 原对象与记号

继续使用
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0),
\qquad u_c(x)=u(x-c).
\tag{1}
$$
同一真实右锚、双 collar 与全部允许平移保持。R303 给完整次数上界 $\deg_c\mathfrak q_{u_c}(V)\le9$。

对于真实 $M=0$ 闭块，令
$$
m(s)=\int_{s_0}^sM(\sigma)d\sigma,\qquad m(s_0)=m(s_1)=0.
$$
为缩短公式，置
$$
m=m_{p_2},\quad b=m_{p_1},\quad t=m_{t_1},
\quad z_1=m_{s_1},\quad
d=h\omega-k,\quad \gamma=h_s,
$$
$$
a=hm,\qquad n=t-b/4,\qquad g=t-b/2.
\tag{2}
$$
这里 t、$z_1$ 是同一个真实八矩累计坐标；与 profile 或射影参数无关。

点态原身份为
$$
m_s=-kh/2,\qquad b_s=-kd.
\tag{3}
$$
采用 R307 的
$$
L=\frac{dm}{4}-h\left(t-\frac b4\right)-\frac{\gamma}{8},
$$
并定义三个实际几何系数
$$
\boxed{
A=\frac{dm}{4}-\frac{ht}{2}-\frac{\gamma}{16},\qquad
B=h\left(t-\frac b2\right)-\frac{dm}{2}+\frac{\gamma}{8},
}
\tag{4}
$$
$$
\boxed{
\Omega=-\frac32hz_1
-d\left(t-\frac b4\right)
-\frac{3\gamma d}{8h}-\frac{d_s}{8}.
}
\tag{5}
$$
$d_s=h_s\omega-k_s/2$ 是原几何约束给的真实导数，不能独立指定。

在母包坐标 $y=x-c$ 中写
$$
v=u'(y),\qquad r=u''(y),\qquad s=u'''(y).
$$
本节以后没有下标的 s 在 profile 积分内只表示 $u'''$；几何积分仍明确写 $ds_{\rm geo}$ 或 $\int_B\cdots ds$。

## 2. 完整三次分子系数

R307 已付完整第三分子导数的五次、四次系数：
$$
Z_5=[c^5](V_Z)_{{\rm third},x}=\frac a4rs,
$$
$$
Z_4=[c^4](V_Z)_{{\rm third},x}
=\frac a8r^2-\frac a2vs+
\left(\frac54ay+L\right)rs.
\tag{6}
$$
八次 self 还需要 $Z_3$，必须从原完整 $W_2,\eta_0$ 保留对应项，而不是从(6)外推。

### 2.1 原二次 history 的完整二次平移项

R255/R73 的八矩式逐项给
$$
\boxed{
\begin{aligned}
[c^2]W_2={}&
m\left(uv-\frac32yv^2-\frac14y^2J_0-yJ_1-\frac14J_2^*\right)\\
&+\left(t-\frac b2\right)(v^2+yJ_0)
+\left(2t-\frac b4\right)J_1+\frac32z_1J_0 .
\end{aligned}}
\tag{7}
$$
所有 J 为同一个真实 u 的原正右积分：
$$
J_0'=-r^2,\quad J_1'=-yr^2,\quad
(J_2^*)'=-(y^2r^2+2v^2).
\tag{8}
$$

式(7)的 $m$ 行来自 $\Phi_{p_2}$，b、t 两行来自 $\Phi_{p_1},\Phi_{t_1}$，最后一项来自 $\Phi_{s_1}$。$\Phi_{p_0}$ 中两个二次尾恰相消，其余原方向的平移次数至多一；没有把它们的低次部分删掉，只是它们不贡献本层。

从 R295 的完整局部恢复式读出
$$
\boxed{
[c^2]\eta_0
=-\frac{3\gamma y+2\gamma d/h+d_s}{16}r^2
+\frac{\gamma}{8}vr-\frac{\gamma}{16}J_0 .
}
\tag{9}
$$
尤其最后一项来自原 $\partial_s(J_e/h)$，不是独立尾常数。

### 2.2 三次项的全部消尾与低阶项

使用
$$
A_Z=(W_2)_x/2+\eta_0/h,\qquad
(V_Z)_{{\rm third},x}
=e(A_Z)_x-\frac h2(W_2)_x+\eta_0,
\tag{10}
$$
以及 R307 已付 $[c^3]W_2,[c^3]\eta_0$，对(7)–(9)逐项微分，得到完整身份
$$
\boxed{
\begin{aligned}
Z_3=[c^3](V_Z)_{{\rm third},x}
={}&\frac a2(us-vr)
+\left(\frac a2y+A\right)r^2\\
&+(-2ay+B)vs
+\left(\frac52ay^2+4Ly+\Omega\right)rs.
\end{aligned}}
\tag{11}
$$

为便于手核，(7)的二阶 profile 导数为
$$
\begin{aligned}
D_y^2[c^2]W_2={}&
m\left(us-2vr+\frac32yr^2-3yvs-\frac12J_0+3y^2rs\right)\\
&+\left(-2t+\frac b4\right)r^2
+2gvs-6nyrs-3z_1rs .
\end{aligned}
\tag{12}
$$
而
$$
D_y[c^2]\eta_0
=\frac{\gamma}{8}vs
-\frac{3\gamma y+2\gamma d/h+d_s}{8}rs.
\tag{13}
$$
把(12)、(13)与 $[c^3](W_2)_x$ 代入(10)，原 $J_0$ 准确相消。式(11)的 $us-vr$、$r^2$、$vs$ 三项均保留，不能只取 $rs$ 最高 jet 配对。

第一分量 $A_{Z,x}$ 的四次系数为
$$
[c^4](V_Z)_{{\rm first},x}=\frac m4rs.
\tag{14}
$$
第二分量次数至多三，故其平方不贡献八次项。因此完整能量本层是
$$
[c^8]E_Z=\int\left(Z_4^2+2Z_5Z_3+\frac{m^2}{16}r^2s^2\right)dy.
\tag{15}
$$
R303 的固定左 collar 至移动包尾至多五次、其余显式外尾至多四次，故没有遗漏另一个八次项。

## 3. 完整能量展开及真实紧边界

沿 R307 定义
$$
\mathcal I=\int r^2s^2,\qquad
\mathcal J=\int vrs^2,\qquad
\mathcal I_1=\int yr^2s^2.
\tag{16}
$$
另记本层暂保的三个普通母包积分
$$
\mathcal A=\int(v^2+ur)s^2,\quad
\mathcal B=\int yvrs^2,\quad
\mathcal C=\int y^2r^2s^2.
$$
它们不是预先为零的量。

直接将(6)、(11)代(15)，只对三项作真实紧端分部积分：
$$
\int r^3s=0,\qquad
\int vr^2s=-\frac13\int r^4,\qquad
\int yr^3s=-\frac14\int r^4.
\tag{17}
$$
$\int r^4$ 的总系数准确为
$$
\frac{a^2}{64}+\frac{a^2}{8}-\frac{9a^2}{64}=0.
$$
于是完整结果为
$$
\boxed{
\begin{aligned}
[c^8]E_Z={}&
a^2\left(\frac14\mathcal A-\frac94\mathcal B+
\frac{45}{16}\mathcal C\right)\\
&+a\left(\frac B2-L\right)\mathcal J
+\frac{9aL}{2}\mathcal I_1\\
&+\left(L^2+\frac a2\Omega+\frac{m^2}{16}\right)\mathcal I.
\end{aligned}}
\tag{18}
$$
这是完整分子平方的原积分身份，特别保留了第一分量平方产生的 $m^2/16$。没有用一个 principal 标签代替其余配对。

## 4. 几何 history 化简与普适八次系数

原 self 对 $E_Z$ 的乘子为 $-k/(8h)$。式(18)第一行的几何因子均正比于
$$
\int_B khm^2ds=-\frac23[m^3]_{s_0}^{s_1}=0.
\tag{19}
$$
它们因此消失；不是把 $\mathcal A,\mathcal B,\mathcal C$ 个别设为零。

R307 已证明
$$
\mathcal D_9=-\frac1{16}\int_BkmL\,ds
=\frac1{16}\int_Bkhmt\,ds+
\frac1{128}\int_Bk\gamma m\,ds.
\tag{20}
$$
从(4)和 L 的原式，
$$
\frac B2-L=-2L-\frac{ht}{2}-\frac{\gamma}{16}.
$$
因此
$$
\begin{aligned}
\int_Bkm\left(\frac B2-L\right)ds
&=-2\int_BkmL\,ds
-\frac12\int_Bkhmt\,ds
-\frac1{16}\int_Bk\gamma m\,ds\\
&=24\mathcal D_9 .
\end{aligned}
\tag{21}
$$
最后一步同时使用(20)的两个相等形式；全部因子准确保留。

定义新的完整真实系数
$$
\boxed{
\mathcal D_8(B)=
-\frac18\int_B\frac{k}{h}
\left\{L^2+\frac{hm_{p_2}}2\Omega+
\frac{m_{p_2}^{\,2}}{16}\right\}ds .
}
\tag{22}
$$
这里 L、$\Omega$ 由同一个原几何及累计矩阵的(2)、(4)、(5)确定，没有新独立状态。

将(18)–(22)代回完整 period，得到
$$
\boxed{
[c^8]\mathfrak q_{u_c}(V_B)
=\mathcal D_8(B)\mathcal I(u)
+\mathcal D_9(B)\{9\mathcal I_1(u)-3\mathcal J(u)\}.
}
\tag{23}
$$
这项恒等不要求先令平台矩阵或 pure 为零；它来自完整 canonical 的原 $F=u^2,\phi=0$ self 代入。

尤其
$$
\boxed{
\mathcal D_9(B)=0
\ \Longrightarrow\
[c^8]\mathfrak q_{u_c}(V_B)
=\mathcal D_8(B)\int(u'')^2(u''')^2
}
\tag{24}
$$
对全部真实紧母包成立。式(24)不是把 R307 结论未经计算向下一层复制；前面保完整配对及消项支付了这一层。

## 5. 全 U 的准确线性观测

固定任意一个非零实紧 $u_*$。在 U 上定义
$$
\boxed{
\mathcal D_8(V)=
\frac{
[c^8]\mathfrak q_{(u_*)_c}(V)
-\mathcal D_9(V)
\{9\mathcal I_1(u_*)-3\mathcal J(u_*)\}
}{\mathcal I(u_*)}.
}
\tag{25}
$$
R303 的次数界使分子每个系数都由十个有限真实平移查询的固定线性组合承载；$\mathcal I(u_*)>0$。

对所有真实生成成本，(23)使(25)与选定母包无关，并等于(22)。线性延拓给全 U 的普适恒等
$$
\boxed{
[c^8]\mathfrak q_{u_c}(V)
=\mathcal D_8(V)\mathcal I(u)
+\mathcal D_9(V)\{9\mathcal I_1(u)-3\mathcal J(u)\}.
}
\tag{26}
$$

同时真平移作用满足
$$
\mathfrak q_{u_c}(NV)=D_c\mathfrak q_{u_c}(V).
$$
比较九次、八次系数，准确得到
$$
\boxed{
\mathcal D_9(NV)=0,\qquad
\mathcal D_8(NV)=9\mathcal D_9(V).
}
\tag{27}
$$
没有把固定圆 period 商假定为平移模；(27)只用于本稿的 universal 原查询。

## 6. 第二条明确真实补偿，保 whole pure 与整九矩

R303 已付
$$
\mathcal K_{\rm top}=\mathcal B_{p_2}(\mathfrak H_6),\quad
\pi\mathcal K_{\rm top}=0,\quad
\mathsf T(\mathcal K_{\rm top})=0,\quad
\mathcal D_9(\mathcal K_{\rm top})=-1080.
$$
其全部 N 导链仍在 $\mathcal R_{\mathrm p0}\cap\ker\mathsf T$。

令
$$
R_9=-\mathcal K_{\rm top}/1080,\qquad
R_8=-N\mathcal K_{\rm top}/9720.
\tag{28}
$$
由(27)，
$$
\boxed{
\mathcal D_9(R_8)=0,\qquad \mathcal D_8(R_8)=1.
}
\tag{29}
$$
$R_9$ 的 $\mathcal D_8$ 值无需假定为零。若要一个准确单位表，定义
$$
\widehat R_9=R_9-\mathcal D_8(R_9)R_8.
$$
则
$$
(\mathcal D_9,\mathcal D_8)(\widehat R_9)=(1,0),\qquad
(\mathcal D_9,\mathcal D_8)(R_8)=(0,1).
\tag{30}
$$
全部列保持 pure 与九矩零；这里的实系数由准确原查询定义，不冒称已经新求积。

所以对任意 $V\in U$，
$$
\widehat V=
V-\mathcal D_9(V)\widehat R_9-\mathcal D_8(V)R_8
$$
在真实函数空间中满足
$$
\pi\widehat V=\pi V,\qquad
\mathsf T(\widehat V)=\mathsf T(V),\qquad
\mathcal D_9(\widehat V)=\mathcal D_8(\widehat V)=0.
$$
从而
$$
\boxed{
c\longmapsto\mathfrak q_{u_c}(\widehat V)
\in\operatorname{Pol}_{\le7}
\quad\text{对所有真实紧母包 }u.
}
\tag{31}
$$
先在响应线性空间作(31)，不把符号系数当作负路径。

若需要实际安装，R297 九个矩阵单位分别减去(30)的两个准确观测，再加两列(30)，得到
$$
(\mathsf T,\mathcal D_9,\mathcal D_8)
(\mathcal R_{\mathrm p0})
=\operatorname{Mat}_3(\mathbb R)\oplus\mathbb R^2.
\tag{32}
$$
R222 的一般有限观测定理于是给 whole pure 与这十一观测的真实同时支付，保全部 mixed 基准和 full-pure 校正后的真实代价；原 Klein 组装给实际闭 hook。

这不扩大成已有一条固定几何的无条件修改，也不自动保持另已指定的 Gaussian 数据、度量或未纳入系统的其他 profile 观测。若使用 R302 的结构保持/增强 IFT，仍须从起点把全部实际目标放入同一个有限系统。

## 7. R303 同一实际几何已具有的全母推论

若一条实际几何已使某个非零母包 $u_0$ 的整个平移 self 为零，则 R307 已给 $\mathcal D_9=0$。再用(26)，其八次系数为
$\mathcal D_8\mathcal I(u_0)$，而 $\mathcal I(u_0)>0$，所以 $\mathcal D_8=0$。

因此无需新增实际校正，同一条几何已经满足
$$
\boxed{
q_B(u_c)\in\operatorname{Pol}_{\le7}
\quad\text{对任意其他真实紧母包 }u.
}
\tag{33}
$$
这给固定母包全中心支付后的第二个普适 shape 接口。它只降次数，并未令其他母包的剩余七次多项式为零。

## 8. 对完整构造的边界

本稿没有把实际圆拆成任意独立的母包参数，也没有给所有微包共同满足完整 period/ruling 的结论。即使 whole pure、平台矩阵以及所写 self 高层已全部支付，仍可能有独立的其他原相容障碍。

特别，若另一个完整证明排除了某个不交 rank-one 微包圆类，本稿的有限控制定理仍作为 U 上的真实线性观测与实际几何控制成立，但不能据此恢复那个被排类的 joint 可解性。是否在新的重叠/非 rank-one 构造中适用，需要按真实原输入与完整相容条件重新判断。

下一尚未付的全 Q 目标是
$\ker\mathcal D_9\cap\ker\mathcal D_8$
上的完整七次及以下层。没有理由先把这些层也填成同一个 $\mathcal I$；其中可能有新的高阶母包泛函、真实尾与有限 $C^2$ 余项。本稿没有执行或预报它们的秩。

作者责任：新公式均由本文显示的原二阶系数、有限手写乘法和真实紧端分部积分得到；没有新增科学运行、程序消元或未披露采样。
