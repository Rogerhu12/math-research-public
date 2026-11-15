# 完整权 −2 字符头部：最小新原数据消费者设计

日期：2026-11-15。**实现设计，不是已经完成的研究计算。** 本地只阅读已发源码、纸面证明和公开导出的 metadata；没有编译研究原式、构造响应、作 profile 评价或计算新的秩。研究实际只在 Rogerhu12/math-research-public 的 GitHub Actions 运行。

数学入口为 [R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)。当前已知 44 维子空间只是完整 U 的下界；本任务不再增加一条孤立的维数下界，而是补齐一个完整字符头部所需的有限生成数据。

## 1. 唯一新目标

固定真仿射权 $\sigma=-2$。生成 R130 十四个归一正规函数族的全部真权 −2 状态系数 $T_{-2}$，并按 R163 从**同一份数据**生成完整平移分母 $D_{-2}$，使

$$
\boxed{
\mathcal H_{-2}
=\frac{U_{-2}}{R_{-2}+\mathsf N U_{-1}}
\cong\frac{R_{-2}+T_{-2}}{R_{-2}+D_{-2}}.
}
\tag{1}
$$

首个消费者完成的具体交付是这个有限原式生成呈示，包括完整输入、所有新增收缩、十四族系数和分母的线性关系。不把“生成呈示完整”称为“商秩已定”，也不称为“正字符已排除”。

R163 已证明：不用另编权 −1 的局部目标，不用重新构造它们的 profile 平移，不用假设十四族全部无修正协变。对低阶，$\mathsf N$ 是 $\partial_\omega-\mathfrak c(m)$；最高层十族才直接用 $\partial_\omega$。

## 2. 输入：只消费已发表原式

所有文件相对于本课题目录。每组输入均需同时绑定公开主报告、terminal publication receipt、run/source、完整 source-hash 对象、gzip/raw 字节数和 SHA，以及每个被用原根的原 SHA。不能只验证 gzip 文件名。

### 2.1 完整原静态局部密度及 W

目录：

~~~text
notes/actions-43645177423-1-local_fourth_quotient/
~~~

run 43645177423，source 2f1b809c0b0abb7a26303d36940edc203815f872。主报告 local-fourth-quotient.json 为 3982 B，SHA256：

~~~text
19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a
~~~

发布回执 SHA256：

~~~text
c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba
~~~

完整导出 local-fourth-quotient-original-expressions.json.gz：

| 内容 | bytes | SHA256 |
|---|---:|---|
| gzip | 657195 | ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace |
| raw JSON | 3518194 | d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1 |

schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，content_scope 为 W-and-local-static-density。实际导出有 430 根：36 个既有 W 原模板和每个模式 197 个 L0 原状态系数。

本次只恢复 L0，作真权 −2 投影及八矩规范化。无需重编 W、v0、原第三势、旧静态收缩或旧静态目标。

该 L0 已用当时逐条真原式身份降去 N0 的 W 分量，故是完整局部静态密度的一个模 R 代表。后面的 L2 可使用 3974 因子中的未降 N0：两者之间只差已证的点态 R 值修正。选择这个 L0 定义同一个 $\Gamma$，在静态层和二次层都使用它；不能在两个层分别换参考值。R163 的结论本来就在 U/R 上，因此这个既有代表可以使用。

旧主报告 completion=output_limit 来自大摘要超限；完整导出及其来源身份已实际成功。输入门应验证导出本身已发表完整，而不是把主报告的摘要超限当作研究原根缺失。

### 2.2 完整 N0/N2 与 v2/v4 的 3974 根

目录：

~~~text
notes/actions-43651096112-1-local_fourth_derivative_factors/
~~~

run 43651096112，source 2259b57065cfad67682f4c4319885fd5334c4f76，lane local_fourth_derivative_factors。主报告 local-fourth-derivative-factors.json 为 5477 B，SHA256：

~~~text
42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927
~~~

receipt.json 为 33580 B，SHA256：

~~~text
6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e
~~~

完整导出 local-fourth-derivative-factors-original-expressions.json.gz：

| 内容 | bytes | SHA256 |
|---|---:|---|
| gzip | 2132064 | 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a |
| raw JSON | 11864540 | 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3 |

schema 为 visible-flex-local-fourth-derivative-original-factors-v1-original-expressions，content_scope 为 unreduced-N0-N2-and-complete-two-mode-v2-v4。

原几何键的准确顺序为

~~~text
h, k, omega, h_s, k_s, h_ss, k_ss, log_h, h_sss, k_sss
~~~

已发 metadata 给：

| 因子 | 完整原记录数 |
|---|---:|
| N0 | 79 |
| N2 | 93 |
| 每个模式 v2 | 665 |
| 每个模式 v4 | 1236 |
| 总原根 | 3974 |

N2 的速度形状 $u^2,uw,w^2$ 分别有 40、31、22 个原状态记录。N0/N2 均未假设属于 W，N2 是全部原 Pacc。该导出已经包含先作真实 s 微分、再将累计 history 的值置零的结果；消费者不得把 history 导数再次置零。

八矩的 m0、m2 标量原系数也已在同一导出的 pointwise_matrix_original_coefficients 中保存，可直接消费。前三个矩阵坐标 p0,p1,p2 的 m2 部分为零，其余五个必须完整保留。

### 2.3 已存五个 A/H 族

目录：

~~~text
notes/actions-43654534244-1-acceleration_layer_mixed/
~~~

run 43654534244，source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b，lane acceleration_layer_mixed。

主报告 acceleration-layer-mixed.json 为 57753 B，SHA256 baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745；receipt.json 为 35241 B，SHA256 3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494。

导出 acceleration-layer-mixed-original-expressions.json.gz：

| 内容 | bytes | SHA256 |
|---|---:|---|
| gzip | 318634 | b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e |
| raw JSON | 1909429 | 7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38 |

直接取完整的十条真权 −2 selected_weight_records，共两个模式二十根；其原状态键和源 hash 保留。不重新从 v4 构造这五族，不重跑 J、J6、G³、旧十个目标或它们的关系。

随后 R162 的公开 actual 43663137188 已严格证明 J6 不在旧
$R_{-2}+\operatorname{span}\{\mathsf N^3G,J,D0\}$ 中，特别不在 R 中。
这不是本消费者重做的目标，也不允许将 c0 置零。新的已知 44 维空间仍只是完整 U 的下界；本设计不以它替代十四族的完整生成范围。

### 2.4 已证明完整 40 维 R−2 原基

目录：

~~~text
notes/actions-43653293263-1-g_translation_successor/
~~~

run 43653293263，source 2f0add61f44365d713abf836beaa8b0be2806a3d。主报告 G-third-translation.json 为 25014 B，SHA256 b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3；receipt.json 为 34619 B，SHA256 a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523。

G-third-translation-original-expressions.json.gz：

| 内容 | bytes | SHA256 |
|---|---:|---|
| gzip | 157782 | 226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e |
| raw JSON | 889438 | eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7 |

只取 R131 已证明保留的四十个原响应列，两模式八十根。原块位置顺序为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49
~~~

不重构五十个旧响应，不重核十条旧依赖，不重评价旧四十列原有理矩阵。G³ 本身不作为一个额外必须分离的新目标；它已属于相邻权的平移像。

### 2.5 复用 D0 实际保存的两条 N2 收缩

目录：

~~~text
notes/actions-43657526246-1-h_axis_sharp/
~~~

run 43657526246，source 0d5df1843fd829e7c09b17afdead930ec4395f34。主报告 h-axis-sharp.json 为 17542 B，SHA256 e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0；receipt.json 为 36161 B，SHA256 1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea。

h-axis-sharp-original-expressions.json.gz：

| 内容 | bytes | SHA256 |
|---|---:|---|
| gzip | 14497 | ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd |
| raw JSON | 80444 | 2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0 |

直接读两模式 new_response_r1、new_response_t1 原根，填入本次统一的收缩 cache：

| 已发响应 | 3974 因子中的原输入 | 原输入 SHA256 |
|---|---|---|
| $\mathcal B_{r_1}(N2[h^{-2}u^2])$ | N2_77，键 (−2,0,0,2,0,0,0,0,0,0) | 7e85cfe207e9cd742863da1d12b5e6825694daa8cc8e2dbe4f09531af438445b |
| $\mathcal B_{t_1}(N2[h^{-4}u^2])$ | N2_38，键 (−4,0,0,2,0,0,0,0,0,0) | e76a8fc4f0c1512a01e63870b956716c3a9a1c6bdf1f6cd3438815eb05bc0b94 |

取这些已有响应的真权 −2 部分；不重作两次旧 contraction，也不重做 D0 的成员或非成员查询。

## 3. 新运算范围：先真权过滤，再作必要收缩

参数坐标沿用原顺序

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)
$$

及真缩放权

$$
(w_a)=(-1,0,1,-3,-2,-2,-1,0).
\tag{2}
$$

真实权由既有 ScalingGrading 的原子规则确定：坐标 $\xi$ 为 +1，j 阶 profile jet 为 −j，完整同右锚原函数加 +1。不能用 h 次数或某个几何单项的名义协变权代替原根的真权。

R89 的完整响应协变及其对第三槽的线性性给

$$
\Pi_{-2}\mathcal B_{E_a}(N_\gamma)
=\mathcal B_{E_a}\bigl(\Pi_{-2-w_a}N_\gamma\bigr).
\tag{3}
$$

因此只构造下表允许的真权第三槽，不生成无关权后再全量展开。

| 二阶方向 | $w_a$ | N2 所需第三真权 | N0 所需第三真权 |
|---|---:|---:|---:|
| p0 | −1 | −1 | 不需要：m2该坐标为零 |
| p1 | 0 | −2 | 不需要 |
| p2 | 1 | −3 | 不需要 |
| r0 | −3 | +1 | +1 |
| r1 | −2 | 0 | 0 |
| s0 | −2 | 0 | 0 |
| s1 | −1 | −1 | −1 |
| t1 | 0 | −2 | −2 |

对 93 个 N2 原记录，上表八种响应是 $\mathcal B_{m_0}N2$ 与
$\mathcal B_{m_2}N2$ 共用的唯一池。L2 生成一次之后，L4 只改变几何乘数和收集键，**不再生成第二套 N2 响应**。

对 79 个 N0 原记录，只需五种 $\mathcal B_{E_a}$。这些是完整
$\mathcal B_{m_2}N0$ 的缺失数据。旧 static full export 没有保存独立降模 N0 或这些单条 contraction cache，故不能声称它们已经存在；但不为此重编原第三势。直接取已保存的未降 N0 原根即可。

未过滤、未去重前的有限候选上界分别为 $93\times8=744$ 与
$79\times5=395$ 个双模式收缩接口，**不是预报实际调用次数**。先将所需第三权投影，空原式直接为零；再按参数方向及投影后的原根 hash 共用完全相同的输入。已有两条 axis cache 先占位。实际调用数和去重清单必须由公开 Actions 输出，不在本地推算或预填。

保留第三原式的外槽及两个内槽颜色。实际调用既有完整 blocks.full_response 和 colored.ThirdOperator，两个相位模式使用同一真第三槽；不能把槽当可独立赋值的 primitives，不能只生成 pure 模式。

## 4. 缺失九个函数族的准确装配

### 4.1 静态规范化与同一个参考映射

从旧 L0 直接投影到 −2，再使用冻结的 R114 reference_coordinates 接口取得原八个有理坐标 $a_i$ 和准确矩阵逆。这里只使用既定 8×8 几何常数接口，不重做任何 W、响应或函数基研究。

计算同一组原参考值

$$
F_i^{\rm ref}=\Pi_{-2}L_0(S_i^*),\qquad
\Gamma_{-2}(M)=\sum_i a_i(M)F_i^{\rm ref},
$$

以及

$$
F_0^{(-2)}=\Pi_{-2}L_0-\Gamma_{-2}(m_0).
\tag{4}
$$

这是旧静态原根的新完整权 −2 归一化，不是旧 m8 尾的重复，也不凭 R124 的 pure 零结论删掉 full mixed。

### 4.2 三个完整速度二次系数

把原 v2 按真实 jet 形状写成

$$
v_2=p\,a+q\,b+Q_2^v(S;u,w).
$$

N2、m2 都是速度二次式，故新增响应不改变 p、q。完整公式为

$$
\begin{aligned}
\widehat Q_2={}&Q_2^v
-(Xp)u^2-(Yp+Xq)uw-(Yq)w^2\\
&-\mathcal B_{m_0}N2-\mathcal B_{m_2}N0-\Gamma(m_2).
\end{aligned}
\tag{5}
$$

对所有 profile 原根先取真权 −2；X、Y 只作用于状态，故与该投影交换。式 (5) 五项矩阵/导数成本全部保留。按 u²、uw、w² 收集，得到三个新族。

每个模式的 v2 原记录完整为：p 134 条、q 110 条、u² 158 条、uw 144 条、w² 119 条，共 665。消费者只恢复真权 −2 所需的原部分；不将原式未出现的记录和尚未处理的记录混为一类。

### 4.3 五个完整速度四次系数

对原 v4 写

$$
v_4=B_hj+B_k\ell+A_{hh}a^2+A_{hk}ab+A_{kk}b^2
+C_ha+C_kb+Q_4^v,
$$

其中 B 为速度一次，C 为速度二次。三个 A、两个 H 族的结果已经保存，不再由这个分支重算。

令 $D_0=uX+wY$，只微分状态系数。R129 给出可直接装配的公式

$$
\boxed{
\widehat Q_4
=Q_4^v-\frac13D_0(uC_h+wC_k)
+\frac13D_0^2(uB_h+wB_k)
-\mathcal B_{m_2}N2.
}
\tag{6}
$$

这是 $Q_4-D_0P_{3,v}$ 的同一原式：先令
$P_{3,v}=(uC_h+wC_k-D_0(uB_h+wB_k))/3$，再代回。没有新增第三势约定。

因此本分支从 v4 只读 B 的四个原系数、C 的六个原系数和 Q 的五个原系数。每个模式分别有 264、444、330 条原状态记录，总计 1038；跳过已有加速度二次三块的 198 条记录，不重新生成五族。

进一步装配时只需 B 的三个对称组合
$\beta_{hh},\beta_{hk}+\beta_{kh},\beta_{kk}$，以及 C 的四个组合
$C_{h,20},C_{h,11}+C_{k,20},C_{h,02}+C_{k,11},C_{k,02}$。
这些是完整原和，不是删掉非对称项；非对称部分已在既有 H1/H2 中保留。

必须顺序施真实 X、Y。尤其

$$
D_0^2=u^2X^2+uw(XY+YX)+w^2Y^2
$$

是作用于状态系数的公式；不能把 XY、YX 合并成二倍其中一个，因为
$[X,Y]=-(2h^2)^{-1}\partial_\omega$。所有 log 链项先求导后选状态系数。

按 $u^iw^{4-i}$ 收集得到五个新族。最后一项使用第 3 节同一 N2 cache，没有新增第二套响应。

## 5. 从单权十四族生成完整 N 分母

此时得到：

| 数据 | 新增 profile 响应 |
|---|---|
| 归一静态 F0 | 无；由旧 L0 线性装配 |
| 三个 Q2 系数 | 第3节 N2八方向、N0五方向 |
| 五个 A/H 系数 | 无；直接消费 R136 |
| 五个 Q4 系数 | 无额外池；复用同一 N2八方向 |

把十四族权 −2 原状态系数建立统一的线性字典。再计算

$$
\mathfrak c_{-2}(M)=
\sum_i a_i(M)\partial_\omega F_0^{(-2)}(S_i^*).
\tag{7}
$$

分母生成式为

$$
\begin{aligned}
D_0^{(-2)}&=\partial_\omega F_0^{(-2)}
-\mathfrak c_{-2}(m_0),\\
D_{2,i}^{(-2)}&=\partial_\omega F_{2,i}^{(-2)}
-\mathfrak c_{-2}(m_{2,i}),\\
D_F^{(-2)}&=\partial_\omega F^{(-2)}
\quad\text{对最高层十族}.
\end{aligned}
\tag{8}
$$

此处 $D_0^{(-2)}$ 是静态平移关系，不是 R153 的轴向目标 D0，也不是水平微分 $D_0=uX+wY$。实现字段应分别命名 static_translation_relation、h_axis_target、horizontal_derivative，避免记号碰撞。

所有 (8) 都输出为十四族原系数字典上的准确有理线性组合，保留完整状态键。对新增的状态标签不能按旧响应支撑裁剪。R163 证明它们模 R 恰为全部 $\mathsf N U_{-1}$；不另外调用任何 G/J/D0 平移 successor。

## 6. 两根忠实表示与商的可判定范围

每个新原系数首先保存完整 −4、−2 两模式。后继需要较小表示时，按 R159 取

$$
(\pi V,\Xi V)
=(V_{-4},\ \text{完整 }V_{-2}\text{ 的 balanced }(2,2)\text{ 部分}).
\tag{9}
$$

该二根映射在完整 canonical U 上联合忠实。不能只取 balanced 根，除非该列的 pure 部分已有真身份支付；也不能因为 J、D0、J6 的个别 pure 身份而宣布所有新族 pure 都在 R。

原根及其线性关系是首个实际的输出。之后可以只对这些**新列**作 sound 归约，保存每条丢列的 fresh 原差，两根分别核零。旧 R−2 四十列仍消费已有原基，不重建或重评价。

当所需独立上界与原式下界确实相等时，才能报告 (1) 的真实维数与对偶坐标。非零 sound 余式不证明非成员，normal form 的 cycle fallback 或预算退出仍为未决。

为了排除正字符，并不一定要先算出精确维数：可用完整生成列表和目前已证的原式关系建立一个**包含全部真实字符坐标的有限外部候选空间**。加入 (8)、R 零条件、非零归一化以及必要正性条件后，若有准确不可行证书，则严格排除该权。若仍可行，只能继续缩小这个必要条件集合；不能把可能忽略真实依赖的形式解当作 U 上的正泛函。

非零归一化必须覆盖全部十四族的生成坐标，例如分成有限个
$\nu_j=\pm1,\ |\nu_i|\le1$ 的盒。只令 $\lambda(J)=1$ 或
$\lambda(D0)=1$ 会漏掉在这两个已知方向上同时为零的字符。

## 7. 实施边界、保存与预算

建议新独占脚本名 literature_character_head_minus2.py，保持全部旧源不变。

复用接口：

| 功能 | 冻结来源 |
|---|---|
| 原式 DAG 子集解码及原 hash | literature_local_fourth_quotient.decode_expressions |
| 小主报告/完整 gzip/publication 绑定 | literature_acceleration_layer_mixed 的 read_bound_json、read_bound_export、check_publication |
| X、Y 及 log 真微分 | 同文件 StateField |
| 真权过滤 | literature_total_P1_scaling_blocks.ScalingGrading |
| 新必需双模式收缩 | 同文件 full_response，原 ThirdOperator |
| 八矩参考坐标 | literature_constrained_static_fourth.reference_coordinates |

关键冻结 SHA256：

~~~text
local_fourth_quotient:
9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0
local_fourth_derivative_factors:
02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf
acceleration_layer_mixed:
271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c
G_translation_successor:
a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406
h_axis_sharp_coefficient:
7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b
constrained_static_fourth:
814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4
total_P1_scaling_blocks:
40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa
~~~

研究入口只接受真实 GITHUB_ACTIONS 与本公开仓库身份。先发表一个小人工接口检查，再由同 lane 运行新原数据装配；人工不读真实研究输入，不能作为真实研究已经完成的证据。

人工范围只针对新增接口：带 log 的水平二阶导数、XY/YX 差、完整式 (5) 的 m2 修正、式 (6) 的三阶 jet 边界、单权收缩的类型过滤、(8) 的负号与同一参考映射，以及 cache 输入身份。不要重复旧 31 条 pure 依赖、40 维原基或旧 forcing 自检。

每个公开实际先输出按输入 hash 和所需权确定的收缩计划，然后只执行尚无已发 cache 的条目。全部新收缩在装配正规族前保存为可复用原式；若预算退出，完整已保存部分可作下一次 consumer 的输入，不得重新计算同一条已成收缩。partial 只能标为 partial，不能据其缺失条目推零。

主报告保持小于 95 KB，含完整 sources/run/phase/completion、输入绑定、计划与实际调用数、十四族覆盖、cocycle/分母记录数、所有逻辑 artifact 的完整 packed/raw hash。原式和呈示保存 gzip，单件小于 5 MB，按一个实际输出总量预算管理；不把大数组或二进制传进对话，不通过 API 分块传送。

原式导出应明确保存：

1. 新收缩 cache 的参数方向、来源 N0/N2 根名及 hash、所需真权、完整双模式原根；
2. 同一组八个静态参考原值及 $\Gamma_{-2}$ 的定义；
3. 十四族的全部真权 −2 状态系数原根及原 SHA；
4. (8) 在上述原系数列表上的准确有理线性组合；
5. 使用的既有四十 R 原列的标签和来源身份；
6. 可选的 pure/balanced 两根，必须同时绑定原完整两模式。

首个阶段不同时加入新有理 profile 采样、旧列原值重算、J6 的第二条成员门、全偶权扫描或正性优化。实际结果一旦给出完整生成数据，下一步立即据其规模构造权 −2 的有限必要字符系统，而非停在一个矩阵规模报告。

## 8. 紧接该数据的主线判定

最先使用已存五族的 R141 PSD 线性形式：

$$
a_0\ge0,\qquad
\begin{pmatrix}a_2&b_1/2\\b_1/2&c_0\end{pmatrix}\succeq0,
$$

以及 R148 的 $\lambda(D0+25J/9)\ge0$。R162 已排除 $J6\in R$，
所以不再继续把这个完整成员身份当作可成功的分支。

完整头部提供一个不同且直接可检验的门：

$$
[J6]=0\ \text{于 }\mathcal H_{-2}
\quad\Longleftrightarrow\quad
J6\in R_{-2}+\mathsf N U_{-1}.
\tag{10}
$$

若 (10) 成立，所有权 −2 字符仍必须满足 $c_0=0$，继而 PSD 迫
$b_1=0$；这与 R162 的非成员不矛盾，因为此处分母增加的是完整平移像。
若 (10) 不成立，则 c0 保留为真实头部坐标，后继必要正性系统仍须处理它。
在完整数据和原式证书产生前，两种结果都不预填。

完整 F0/Q2/Q4 数据的意义是，此后可以引入**同一个**八矩乘子 μ，构造 R140 的静态和实际路径必要测试，不再仅在 A/H 五族上猜字符。每条完整路径的三个时长系数必须满足

$$
A\ge0,\qquad C_4\ge0,\qquad B+2\sqrt{AC_4}\ge0,
$$

不能单独要求 B 非负，也不能对不同路径换 μ。有限必要测试的准确不可行只排除这个权；可行不能代替全路径正性。

本设计不宣称五族的有限名义权范围就是完整 U 的权范围。排除权 −2 后仍应按完整原系数的真实权库存决定下一个偶权，不从已有局部下界推全成本锥结论。闭锥、实际有限有符号成本、完整 period/ruling 和主课题最终几何条件也继续保持区别。

## 9. 已实现接口与人工开发状态

独立新源码 literature_character_head_minus2.py 已实现上述单权生成任务，
58856 B，SHA256：

~~~text
fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11
~~~

源码没有新增原式 rank、原有理 profile 评价或正性优化分支。消费器只生成本设计的原数据和线性呈示，后继问题通过明确字段继续。

新增 13 项小人工接口检查已经本地实际通过；没有读取真实研究输入。
开发主报告 character-head-minus2-artificial-development.json 为 8215 B，
SHA256 09a3d25f85445cb8193e774d02af9da4bc4236ff546fba304ddf8eeee7c5b00b；
用时 0.010400507002486847 秒，峰值 RSS 17.125 MiB。此前 py_compile 通过。
人工覆盖真实水平不交换导数及 log、两种正权势、单权响应过滤、
跨 N0/N2 cache 共用、partial artifact 的原式往返及未完成不作零、
L2 两个 N 项与同一 Gamma 符号、低阶平移的负 cocycle、h=1 前的 log
缩放导数等新增接口。人工不宣称真实十四族已经生成。

同一 Actions lane 建议名称 character_head_minus2，先人工，再实际：

~~~sh
python topics/visible-flex-new-mechanism/scripts/literature_character_head_minus2.py \
  --toy-only \
  --output WORK/character-head-minus2-development.json

python topics/visible-flex-new-mechanism/scripts/literature_character_head_minus2.py \
  --output WORK/character-head-minus2.json \
  --max-seconds 240 --memory-mib 1024 --checkpoint-every 8
~~~

WORK 由公开 workflow 设置为该 lane 的实际输出目录。五组输入使用本稿第 2 节
已绑定的缺省目录，可分别用 static/factors/acceleration/response/axis-directory
参数改变本地存放位置，但文件字节、run/source、receipt 和 schema 必须仍是已绑定身份。
所需 sparse 目录正是第 2 节五个 actions 目录，另含 scripts/results。

实际输出：

- character-head-minus2.json：小主报告，完整输入、来源及进度；
- character-head-minus2-complete-report.json.gz：完整报告；
- character-head-minus2-original-expressions.json.gz：同一逻辑原式 artifact，
  随 checkpoint 原子替换，先是 partial cache，最后才可为完整十四族呈示。

完整 artifact 的 normal_family_records 保存十四族两模式原根；
head_translation_presentation 保存 (8) 在同一原系数字典上的准确有理组合。
static_translation_reference_coefficients 和
static_scaling_reference_coefficients 还保存八个参考态的
$\partial_\omega F_0$ 及 $(h\partial_h-\omega\partial_\omega)F_0$ 原系数组合，
为同一个八矩乘子的后继字符条件提供数据。第二种导数也先完成全部 log 链式微分，
再在 h=1 取值。

cache_records 与 contraction_plan 一起绑定每项来源 N 原根、真正第三权、二阶方向、
结果权和完整模式原 SHA。恢复 partial 时，必须提供七个完整入口：
resume-report、resume-publication、resume-export、resume-report-sha256、
resume-publication-sha256、resume-run、resume-commit；恢复只接受同一冻结源码、
同一原输入与同一真权计划的公开 artifact。已经完成的头部呈示应直接供新消费者使用，
不以 resume 再次生成。没有已发 cache 的条目才调用新的 contraction。
