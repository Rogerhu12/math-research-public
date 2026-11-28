# 半波种子的一次宽度对照：完整来源、位置账与符号反转边界

2026-11-28。本文建议只准备一个独立完整对照：沿用 run22 的全部运行源码、固定参考与预算，将相对边层总长从 $b/S=1/2$ 改为 $5/8$，保留 $\delta=1/32$ 和两个初始阻尼 $.01$。本文不把该选择表述为 reach、Gram 或握持的已证改善，也不把准备参数当成已启动运行。

建议名称为 fixed-fejer-paired-halfwave-bfiveeighths-first。全部137个科学来源角色、18个当前运行体、原完整157词科学与7词纯读取入口均共享 run22 原件。唯一科学数值改变是边层宽度；完整输出目录、step标识和读数路径另取新名。root 决定是否及何时实际执行，本文不改 refs 或队列。

## 1. 已有事实及它们没有给出的信息

以下是各自真实初始有限屏幕的读数，来自已公开的完整实际记录；它们不是连续全域证书，不是同一个模型上的三次迭代。

| 运行与机制 | $b/S$ | reach 族 $g$ | distance_plus 族 $g$ |
|---|---:|---:|---:|
| 19：每中央区间完整波 | $1/2$ | $0.9684249942095058$ | $0.005863061771032241$ |
| 21：每中央区间完整波 | $5/8$ | $2.541916739245917$ | $-0.05389631415885021$ |
| 22：配对半波 | $1/2$ | $0.5305849371949052$ | $0.11391238912344381$ |

19、21分别见已刊 [run19完整事实](2026-11-27-run19-complete-bhalf-launch-and-continuation.md)、[run21完整事实](2026-11-27-run21-complete-five-eighths-launch-and-continuation.md)。22见 [run22完整事实](2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md)与 [真实有界index](2026-11-28-public-actions-46090913581-1.md)。本次亲读的22固定index为提交 a236a56e25799e1aace2bb3300c250f71d7cd351 下的完整原件：50,179 B，SHA256 c235e12015495f77221618b798a439eb9bfbed36b4a9faa59d546a6b72fff2da，Git blob 42af20c0a8945837b7dcb72610f572240e914489。index记录时刻为2026-11-28 01:25:19 UTC，数学事件为2026-11-28T01:24:50.545031+00:00的 current-geometry-returned；本次没有将这个时刻改称初次几何完成时刻。

该22记录的完整模型为 6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef；初点为 7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，Phi为681.6517423825409，有限相对Gram为0.40616525311769985，accepted为0，完整科学report仍false。实际子科学来源提交为 c6517a030888df2bf0ca51efade67b7693102785、launcher为6fd57ab、PID3541。这个进行中的观测点不能送给准确费用、父迁移或完整mesh。

三组标量没有给出真实最大曲率的径向胞、材料角、分支、$K$与$D$的独立值，也没有给出准确 $r,d,\lambda$ 和它们的全角导数。因此不能从表内反推出“21一定由中央段控制”或“22一定由端层控制”。本文未重算这些量。

## 2. 必须先按真实源解释两个瓶颈

本次读完整 so3_fixed_fejer_halfwave_geometry.py 的 GeometryScreen._point_geometry、_amplitude_values 与 scan：

- 曲率对每个实际点调用原完整 curvature_cotangent 的两个 principal 分支；没有可在此直接换掉的二阶 jet 三角上界。
- 有限屏幕记录 $D_{\rm screen}=\max(2,2|H|,2\max|F|)$，reach族为 $.03D_{\rm screen}K_{\max}-.992$。本文保留这个真实工作定义；它不等于已经付清的全闭面 reach 证明。
- 令 $X=1+\sum_{m=1}^{M}c_m$ 是全部当前core给出的见证半轴，$q_\pm=(0,\pm X,0)$，$L_{\rm wit}$ 是原见证下界预算，则
$$
g_{\rm dist,\pm}(s,\phi)=1-\frac{|F(s,\phi)-q_\pm|^2}{L_{\rm wit}^2}.
$$
整个扫描取这些量的最大值。因此 distance_plus 要求整像与固定见证点分离，不能把它误读为“越向内越好”的径向上界。
- body_diameter族为 $4|F|^2/B^2-1$。帽直径与高度族分别为 $4(R^2+H^2)/B^2-1$ 和 $(H_{\rm floor}-H)/L_{\rm wit}$。

这些公式说明：在固定当前core、$H,R$时，宽度本身不改变最后两项公式；但 body、distance、Gram 和曲率仍依赖完整新的 $F$及全部六jet。完整优化还允许当前core、$H$和全部旋转通道变化，不能把这个固定坐标的说明升级为新优化结果。

## 3. 保持不变的对象和唯一改变的输入

采用 [R724](../results/R724-paired-halfwave-central-seed-and-complete-source-identity.md) 的同一配对半波机制，第一中央段用 $+\lambda h_\delta(t/2)$，第二段用负号。固定的准确标量函数、Fejer材料图、参考core、节点定义、$S,R,H_0$、固定度量
$$
g=ds^2+a(s)^2\,d\Theta_0^2
$$
和所有原自由变量均不因本次宽度参数改变。每个新runner仍须实际构造并严格绑定自己的完整输入；这里没有预填其whole文件SHA、模型、点、根、报告或证书。

总支持长度 $L=7S/8$。两中央段等长，四端层各长 $b/4$：
$$
L_c=L-b,\qquad \ell=(L-b)/2.
$$
新 $b=5S/8$ 时，四端层各长 $5S/32$，$L_c=S/4$、$\ell=S/8$，中央区间为
$$
[3S/16,5S/16],\qquad[11S/16,13S/16].
$$
$\delta=1/32$ 的全部六片归一化切点仍为
$$
0,\ 1/16,\ 7/16,\ 1/2,\ 9/16,\ 15/16,\ 1.
$$
每个准确物理切点仍按各自中央区间的完整affine公式生成。原源从准确参数计算这些切点；本对照没有删除片、变量或角。

这仍严格满足原 SeedParameters 的 $0<b<7S/8$ 与 $0<\delta<1/8$。这里只说明定义域合法，不替代均值根存在、完整normal32或全连续几何证据。

## 4. 半波下的宽度竞争：两项收益与一项明确代价

本节只应用已登记的 [R721](../results/R721-supported-seed-width-and-profile-sensitivity.md) 和 R724，不登记重复结论。以下微分式要求所讨论的准确均值根分支已经存在且正则、$0<r<1$、投影架分母非零，并在比较区间保持这些条件。

令 $c_\delta=1/4-\delta$，准确幅度为 $A_\delta(\lambda)=r$。配对半波的中央径向主项是
$$
U_c^{\rm half}=\frac{\lambda}{2c_\delta\ell}
=\frac{\lambda}{c_\delta(L-b)}.
$$
因此由 $b=1/2$ 到 $5/8$，
$$
\frac{U_{c,\rm new}^{\rm half}}{U_{c,22}^{\rm half}}
=\frac32\,\frac{\lambda_{\rm new}}{\lambda_{22}}.
$$
半波在同宽度下把原完整波这一主项减半，但宽度继续增大仍会压缩中央段。不能删除这个 $3/2$。

R721的端层转向界含
$$
\frac{U_s}{\nu}+\frac{15}{b}\tan(\theta_{\max}/2).
$$
只看显式 $1/b$ 前因子，本次乘 $4/5$。实际 $U_s,\nu,\theta_{\max}$ 随端层扫过的原参考和新均值方向变化，不能直接复用旧值后宣称实际端层曲率降低20%。

对配对半波中间位移，记
$$
J_\delta(\lambda)=\int_0^1\sin(\lambda h_\delta(t/2))\,dt>0.
$$
中间横移量是 $\ell J_\delta(\lambda)w$，且 R724 给 $J_\delta\le\sqrt{1-r^2}\le1$。新长度前因子乘 $2/3$；只使用共同粗界 $J_\delta\le1$ 时，相应绝对预算从 $3S/16$ 降到 $S/8$。真实横移比却是
$$
\frac23\,\frac{J_\delta(\lambda_{\rm new})}{J_\delta(\lambda_{22})},
$$
仍未确定。宽度变化还会改变位移的共同纵向部分与四端层，不能把这个单项预算当成全位置误差或 distance_plus 的单调性。

完整均值变化依旧满足 R721 的
$$
J_{\rm mean}v_b=v-B_b,\qquad
\lambda_b=\frac{r_b}{A_\delta'(\lambda)}.
$$
这里 $B_b$必须包含四个移动端层的参考采样项。特别
$$
\partial_b\log U_c^{\rm half}
=\frac1{L-b}+\frac{r_b}{\lambda A_\delta'(\lambda)},
$$
以及中间横移标量的导数
$$
\partial_b(\ell J_\delta)
=-\frac12J_\delta+
\ell J_\delta'(\lambda)\frac{r_b}{A_\delta'(\lambda)}
$$
都依赖真实根的响应。没有已付的 $r_b$、$J_\delta'$及共同分母时，这些式子不定号。

对固定物理 $s$、且保持在某一中央片内部，$a_i'(b)=1/4$、$\ell'(b)=-1/2$，所以
$$
t_b=\frac{2t-1}{4\ell},\qquad
\alpha_b=\varepsilon_i\{\lambda_b f_\delta(t)
+\lambda f_\delta'(t)t_b\}.
$$
完整切向量宽度导数还含
$$
T_b=\cos\alpha\,d_b+\sin\alpha\,w_b+
\alpha_b(-\sin\alpha\,d+\cos\alpha\,w).
$$
全位置导数从所有径向片积分；移动接点的内部边界项由真实连续接合相消，不能遗漏各片内部的 $t_b$或移动参考项。固定core下
$$
\partial_b g_{\rm dist,\pm}
=-\frac{2(F-q_\pm)\cdot F_b}{L_{\rm wit}^2},\qquad
\partial_b g_{\rm body}=\frac{8F\cdot F_b}{B^2}.
$$
它们给出判别实际改善所需的明确向量量，却不能由公开的三个g标量代替。

## 5. 交换半波先后不是现有相位重标记，但没有已知改善符号

固定同一个合法准确根、宽度和profile，分别令符号次序为 $(+,-)$ 与 $(-,+)$。定义
$$
A(t,\lambda)=\int_0^t\sin(\lambda f_\delta(u))\,du.
$$
第一中央段令 $a=\ell A(t,\lambda)$；两段之间令 $a=\ell J_\delta$；第二中央段令 $a=\ell[J_\delta-A(t,\lambda)]$；两段包围区以外令 $a=0$。则 $a\ge0$，准确core锚定位置有
$$
F_+=C+aw,\qquad F_-=C-aw,\qquad
C=(F_++F_-)/2.
$$
均值、$\lambda$及每段同位的 $|T_s|$相同；两段合并后的切向量值域相同，位置及其角jet一般不同。具体
$$
F_{+,\phi}-F_{-,\phi}=2(a_\phi w+aw_\phi),
$$
$$
F_{+,\phi\phi}-F_{-,\phi\phi}
=2(a_{\phi\phi}w+2a_\phi w_\phi+aw_{\phi\phi}).
$$
因此 Gram、完整主曲率和跨片距离并不由局部 $|T_s|$的相等锁定。

同一固定见证 $q$ 的距离差准确为
$$
|F_--q|^2-|F_+-q|^2=-4a(C-q)\cdot w.
$$
若某点的 $(C-q)\cdot w<0$，反转符号在那里增加距离；反号则相反。虽然 $e_r\cdot w>0$，$w$一般也有竖直分量，这不足以控制右侧。必须覆盖整个新旧像面和固定帽，不能用一个局部有利符号替代整像最大族。

这两个recipe不是 R724 已有的正交/物理相位协变。对任何同时作用于完整原数据的正交变换，
$$
w=\frac{e_r-(e_r\cdot d)d}{|e_r-(e_r\cdot d)d|}
\quad\longmapsto\quad Ow.
$$
变换保持每个固定径向区间的符号；若在同一材料角还要求固定 $d$ 与 $e_r$，便不能又把非零 $w$变为 $-w$。物理相位使用同样的协变和准确材料重参数化，也不交换两径向区间。径向反转会交换非圆core端口与圆帽端口，不能作为本固定core/帽/握持模型的原端口保持重标记。原水平半转、平面反射和上下片反射同样不自动交换这两个径向符号。

这个结论精确排除的是“已有全数据刚体协变或端口保持的相位重标记”。本文没有据此证明两张未来未标记像面不可能偶然全等；那需要完整像面证据。也没有把seed的位置恒等式自动迁给不同参考校准下的实际32阶段normal解。

所以反转符号是一个真实但尚无有利全域方向的构造自由度；当前源与准确费用将 $(+,-)$作为严格定义。选择它会要求独立完整seed、真实六片公式及完整来源传播，不能只换显示标签。本文不准备该第二候选。

## 6. 为什么先只选半波5/8，而不同时改profile或符号

这个选择是有明确定量竞争的单变量对照，不是最优性结论：

1. 相比22，它只改变宽度，检验更宽端层和更短中间横移预算能否改善当前reach与见证距离；中央压缩代价完整保留。
2. 相比21，它在同一宽度使用已经定义清楚的半波中央机制；不能沿用21的K、位置或分母，但能检验此前完整波失败的宽度是否因机制变化而重新可用。
3. $\delta$保持 $1/32$。R721已说明profile改变对中央斜率、幅度和更高径向导数有竞争；当前没有必要把第二个数值变量混入。
4. 符号次序保持原 $(+,-)$。上节给出的真实距离差尚无全域定号，不能据“向内”猜测全目标改善。

这里最需要的未来返回是新场自身完整统计和六族几何，随后按已有准确链读取同一点、完整根packet、全32阶段、全径向/全圆与完整端口。若公开完整报告包含最坏位置和两principal曲率分支，就能据其真正位置区分端层、中央和角向/混合控制；本文不要求另加一个诊断或测试阶段才能开始原完整科学。

## 7. 无损参数共享与未来责任

两个新ready分别内嵌完整科学step和完整pure step。它们共同引用 run22 的完整94,317 B科学ready、84,075 B纯ready、30,196 B读数对应表、23,548 B参数总表和67,013 B运行来源总表，使用精确文件身份和JSON pointer恢复全部历史与全部当前来源。没有机械复制三份相同祖先metadata，也没有删掉其内容。

新的step保留原157/7全部参数词、458/445全部正式selector、48实时selector、全部outputs/cleanup与完整科学预算。仅科学宽度值、fresh namespace、step id和相应读数路径改变。所有旧五个受支持CLI peer及全部外部未知责任原样保留；run22仅另作为已知真实运行但未取得完整父材料的外部来源记录，不塞入未支持的typed迁移CLI。

新runner、真实输入whole身份、模型、point、accepted/typed历史、报告、final13、根packet、连续费用和全部证书均为null或未声称。现有22的进行中7e06观测不会被填入这些字段。全部运行源码原字共享；没有新AST/fixture/扫描、科学预门或缩短的求解阶段。root独占发布与队列。

## 8. 完整来源定位

- 当前seed：scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py，43,697 B，SHA256 cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0，blob cc877246e546b8294826ad38d33b3eb2f7434f25。读取全部 SeedParameters、paired_halfwave_definition、_cutoff_and_profile、_means、evaluate 与model。
- 当前有限几何：scripts/resume_20261126/so3_fixed_fejer_halfwave_geometry.py，88,164 B，SHA256 494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b，blob 602ef5d9e322a3301ede97a811fa9b10044bc61b。
- R721：results/R721-supported-seed-width-and-profile-sensitivity.md，24,655 B，SHA256 14a0b6205f89fa68e5ec04de5960ca19859fccfebac015e01fadb02f75c7363a。本文只引用其已登记宽度/profile公式。
- R724：results/R724-paired-halfwave-central-seed-and-complete-source-identity.md，25,314 B，SHA256 fea22bde71c3780bead8b7448c5fc057e64f8e6429f97c1b3155e1d13e32f878，blob e2dbf61239c0092025ef8a5c0f6cac80b4e87d83。
- 完整137来源/18运行体：computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json，67,013 B，SHA256 6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638，blob 4f20af6e3663bdf69aca7193bc29624dc706411c。
- run22完整参数总表：computations/fixed-fejer-paired-halfwave-bhalf-complete-parameter-delivery.json，23,548 B，SHA256 ed050212100d597aa6e43af283aad16ad46a7819f73b2db32e4c21e2ce76c05d，blob 6e42ab000ab2f74a4628bf340669c23bace8a410。

本说明只做完整源码审读、已有数学的明确应用和无损参数准备；未执行任何新的数值科学，也没有新的成功、连续证书或全等/不全等数值结论。
