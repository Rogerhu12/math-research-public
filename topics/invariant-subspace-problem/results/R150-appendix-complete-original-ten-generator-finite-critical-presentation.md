# 原 Bell 归一临界理想的完整十生成元有限表示

作者：Astra-ISP-789f / root、normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

## 1. 原问题、系数环及结论

沿用[原匹配 Bell 的全局双线性坐标](R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md)，令
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),\qquad
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4].
$$
原 Bell 多项式准确变为 $b=y\cdot w$。原完整十七梯度通过已付全局多项式坐标变换和可逆 Jacobian 运输，等价于
$$
F_i=\partial_{u_i}R',\qquad
W_j=\partial_{w_j}R',\qquad
Y_j=\partial_{y_j}R'.
$$
不倒置任何 $y,w$ 参数。原第三矩 Schur 消去的常数单位与全部原来源沿先前证明保留。

记
$$
I=(F_0,\ldots,F_4,W_0,\ldots,W_5,Y_0,\ldots,Y_5,b-1)\subset S.
$$
本次实际完成一个有完整原来源的10×68有限矩阵；其11个矩梯度列又由已付精确二次公式明确落在其余列张成的子模中。因此取原输出的字面57列子集，得到
$$
\mathcal P_{57}:S^{57}\longrightarrow S^{10},\qquad
\operatorname{coker}_S\mathcal P_{57}\cong S/I.
\tag{1}
$$
这57列的全部条目对五个 $u$ 变量至多一次。实际回执仍准确记录10×68；删列结论是下文的原来源恒等推论，不冒称另一次运行。
每个矩阵条目以精确算术表达式保存，叶节点绑定实际原参数多项式的完整文件与坐标；没有参数特化、截断或参数逆。该表示保留全部参数关系，并不声明十个生成元自由。

原十个单项式为
$$
m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
实际保存五个完整10×10乘法代表 $N_i$、五个11×10原来源 $S_i$，满足
$$
u_i m=mN_i+(F_0,\ldots,F_4,W_0,\ldots,W_5)S_i.
\tag{2}
$$
全部50条来源均已从中间的 $\operatorname{NF}(W_j)$ 运输回原 $F,W$；没有丢失原五源校正。

## 2. 精确 lower 回填及来源

[十六条完整三次来源](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)已实际逐全部560个原 $E$ 坐标乘回。配合[完整十二低次正规式](R150-appendix-complete-original-twelve-gradient-low-normal-forms-over-all-parameters.md)，写
$$
G=(F_5,\operatorname{NF}(W)_6)=q+Lu+c.
$$
$L$ 为11×5、$c$ 为11×1，全部66条参数多项式来自原实际文件。本次又核验每个原单项式的完整十八变量坐标，确认其中没有 $u$，并分别满足权2、4。

将15个二次单项式分为11个被消去项 $z$ 与四个保留项 $v$：
$$
G=Uz+Vv+Lu+c,\qquad
U=\begin{pmatrix}Q_5&P_E\\0&C_6\end{pmatrix},\qquad
D=U^{-1}=
\begin{pmatrix}
Q_5^{-1}&-Q_5^{-1}P_EC_6^{-1}\\
0&C_6^{-1}
\end{pmatrix}.
$$
两固定常数逆的全部25+36个原右逆产品本次均重新核验；两原方块及全部135个 top 系数又与原十一二次字典逐项比较。于是
$$
z=-D(Vv+Lu+c)+DG
\tag{3}
$$
准确给出全部15个二次单项式的表达
$$
a=\rho_a+\sigma_aG.
$$
四个保留项的 $\rho$ 是相应单项式自身，$\sigma=0$。

对任一已核三次边界单项式 $t$，原固定常数来源
$$
t=\sum_{g,k}X_{gk}u_kq_g
$$
代入 $q_g=G_g-L_gu-c_g$ 及(3)，即
$$
\begin{aligned}
t={}&-\sum_{g,k,a}X_{gk}L_{ga}\rho_{u_ku_a}
-\sum_{g,k}X_{gk}c_gu_k\\
&+\left(\sum_{g,k}X_{gk}u_ke_g^{\mathsf T}
-\sum_{g,k,a}X_{gk}L_{ga}\sigma_{u_ku_a}\right)G.
\end{aligned}
\tag{4}
$$
符号全部按此式保存。16条(4)覆盖五个 $u_i$ 乘四个 $v_l$ 的全部20个乘积，重复三次单项式共用同一条已核来源。

若 $\operatorname{NF}(W_h)=W_h-\sum_iH_{hi}F_i$，一条中间来源 $(s_F,s_W)$ 严格运输为
$$
s_F^{\mathrm{orig}}=s_F-H^{\mathsf T}s_W,\qquad
s_W^{\mathrm{orig}}=s_W.
$$
$H$ 的每个原条目本次均核为固定 $E$ 常数。以上给(2)全部原来源。每条三次来源的 $u$ 次数至多1；系数始终只用固定 $E$ 常逆。

这里的全参数证明是(3)、(4)的精确通用代入：其假设是已核固定常数乘回和原完整参数多项式身份。程序没有虚称将72,436位常分母与全部参数多项式乘积完全展开后再逐巨大系数比较；实际回执明确记录这一差别。

## 3. 原六条 mean 与完整有限矩阵

[六条原均值关系](R150-appendix-complete-six-mean-relations-and-nine-bell-normalized-generators.md)给
$$
\widehat Y_i=\sum_{a=0}^{9}m_a h_{ai}(y,w)
=Y_i-\sum_{k=0}^4\nu_{ik}F_k-\sum_{j=0}^5\mu_{ij}W_j.
\tag{5}
$$
本次把六个大文件按单个原 monomial/coefficient pair 流读，核完整压缩与逻辑 SHA，保留全部十坐标 $h_i$ 和全部11来源 $\nu_i,\mu_i$。没有仅取二次块或丢低次参数项。

$\mathcal P$ 的68列依次为：

1. 五个 $u_iI_{10}-N_i$ 的全部50列；
2. 十一列 $G_g(u)e_0$；
3. 六列 $h_i$；
4. 一列 $(b-1)e_0$。

这里中间的 $G_g$ 仍完整保留，其到原 $(F,W)$ 的常数可逆运输也保存。每一列均有按
$$
(F_0,\ldots,F_4,W_0,\ldots,W_5,Y_0,\ldots,Y_5,b-1)
$$
排序的18项原来源；50+11+6+1列没有省略。

先证明完整68列版本的同构。定义
$$
\pi:S^{10}\longrightarrow S/I,\qquad e_a\longmapsto m_a\bmod I.
$$
(2)、(5)及原 $G,b-1$ 来源表明 $\pi\mathcal P=0$，故有诱导满射
$\bar\pi:\operatorname{coker}\mathcal P\to S/I$。

反向，实际九条字面路径是
$$
N_ie_0=e_{u_i},\qquad
N_1e_{u_4}=e_{u_1u_4},\quad
N_2e_{u_3}=e_{u_2u_3},\quad
N_2e_{u_4}=e_{u_2u_4},\quad
N_3e_{u_4}=e_{u_3u_4}.
$$
结合 $u_iI-N_i$ 关系，得到每个 $e_a=m_a(u)e_0$。因此 cokernel 是循环 $S$ 模。
十一列 $G_g(u)e_0$ 杀掉全部矩梯度；六列(5)再杀全部 $Y_i$；最后一列杀 $b-1$。
所以 $1\mapsto e_0$ 定义 $\tau:S/I\to\operatorname{coker}\mathcal P$。
两复合映射在 $1,e_0$ 与全部 $e_a=m_a e_0$ 上都是恒等，从而互为逆。

这证明使用的是 $B[u]$ 上的有限 presentation。没有用“十生成”推出“十步稳定”，也没有在自由 $B^{10}$ 上预先假定五个 $N_i$ 可交换。

### 3.1 原11列的明确消去及10×57线性表示

记原边界列
$$
R_{i,a}=u_i e_a-N_i e_a.
$$
令 $e_{u_j}$ 表示十基中第 $1+j$ 轴，对普通二次单项式 $u_i u_j$，取 $i\le j$，写
$$
\rho_{ij}=N_i e_{u_j},\qquad
K_{ij}=R_{i,u_j}+u_iR_{j,0}
=u_i u_j e_0-\rho_{ij}.
$$
按普通单项式系数（对角项不额外乘2）写
$$
q_g=\sum_{i\le j}q_{g,ij}u_i u_j.
$$
(3)的方块逆恒等式 $UD=I$ 给
$$
\sum_{i\le j}q_{g,ij}\rho_{ij}
+\sum_jL_{gj}e_{u_j}+c_ge_0=0
$$
作为自由 $B^{10}$ 中的精确向量恒等式。因此在原自由 $S^{10}$ 中已有
$$
G_g(u)e_0
=\sum_{i\le j}q_{g,ij}\bigl(R_{i,u_j}+u_iR_{j,0}\bigr)
+\sum_jL_{gj}R_{j,0}.
\tag{7}
$$
这显示全部11个 $G_g(u)e_0$ 列本来就属于50个边界列生成的子模；来源显式保留，只含固定 $E$ 常数、原 $L$ 与一次 $u$。

故从实际68列中保留零起始编号 $0,\ldots,49,61,\ldots,67$，即50个边界列、六条 mean 和 Bell−1，就得到(1)的 $\mathcal P_{57}$。其源矩阵也取相同原列子集即可，没有任何参数主元假设。

$N_i,h_i,b-1$ 的条目均属于 $B$，所以 $\mathcal P_{57}$ 只有边界列中的 $u_i I$ 含 $u$，且至多一次。这是一个完整的线性于五个 $u$ 的有限表示。它仍可含参数扭子与非平凡核；没有声称为自由十模或已经判空。

## 4. 所有交换子及非自由关系仍保留

实际还保存10对 $(i,j)$ 的全部100个交换子列和对应原来源。由(2)直接相减得
$$
m(N_iN_j-N_jN_i)
=(F,W)(S_jN_i+u_jS_i-S_iN_j-u_iS_j).
\tag{6}
$$
矩阵和原来源的两边完整保留。(6)是商中的关系，并不声称左边在自由十维坐标中为零。

等价地，可研究 $B^{10}$ 中由这些关系、原生成元与六条 mean、Bell−1 出发的最小 $N_i$ 稳定子模；但本次没有计算其稳定闭包，也不规定免费停止步数。有限表示(1)本身不需要完成该稳定迭代。

[原三阶子式理想](R150-appendix-original-mean-three-minor-ideal-is-the-cube-of-the-mean-ideal.md)仍给 Bell=1 上的完整3×3子式开覆盖，因此可在各真开集把表示进一步缩为至多七个模生成元。rank3例外保留，不能由此宣称四个二次生成元总能全部消掉，也不能把局部七生成提升为全局自由七模。

## 5. 实际执行、内存修正与输出身份

首版和第二版均实际 exit137，没有完整最后回执。第二版已经避免代数式扁平化，最后打印全部50边界列与第一个 mean 文件；当时最大常驻228092 KiB。未完成版本没有被改写为成功。

v3 对大 mean 文件先完整流核两个 SHA，再每次仅解析一个原 monomial/coefficient pair。算术图引用更早节点，不复制展开式；封存也用流式 JSON→gzip。数学来源和全部参数门保持。

v3 实际 exit0，34.88705002300412秒，最大常驻141968 KiB。实际通过：

- 34个原输入文件的完整绑定与两个 SHA；
- 61个固定常数逆产品和135个 top 系数比较；
- 36114个完整原参数 monomial/coefficient 支持、权重检查；
- 全16条来源回填、全部50个原乘法来源、九条字面循环路径；
- 全68列有限表示及全部100个交换子原来源；
- 105774个有类型、无前向引用的精确算术节点。

binding：
~~~text
11473d55e9cf229685bcbebf59fe30fea9c2b00e8fa225bac6d3d0ca71b7ef76
~~~

| 临时对象 | 字节数 | SHA256 |
|---|---:|---|
| 实际小回执 | 2049 | 654125e66289082b33d94836fc7a5cd782becfec5d9b2675f05d6f76bd89a303 |
| 完整算术图 gzip | 634785 | 9d3f03d2746cfb9a1bb3f872f56822ca8136e982cfdcf0cddd666c58aa573a8a |
| 算术图逻辑内容 | 4405032 | 9a49a0740c23bfd2dd6e3d9deec51eec7290a5b40793075c706976d4a2dc81ce |
| 实际68列有限表示 gzip | 12551 | f008cb6bfbb51d0efbe929399b18ef2d7384cb7739b24dc942b25b016211259c |
| 实际68列表示逻辑内容 | 32532 | e96e100317ead08232c6e4d6ef2a4dc1a33339a3909cb5e761d02983b709957a |

可重现小文件：

- [最终v3源](../notes/2026-11-16-r150-original-ten-generator-border-slp-and-critical-presentation-v3-789f.py)；
- [输入与原父文件 pins](../notes/2026-11-16-r150-original-ten-generator-border-slp-inputs-v3-789f.json)；
- [精确图语义与执行接口](../notes/2026-11-16-r150-original-ten-generator-border-slp-interface-v3-789f.md)；
- [执行身份与失败边界](../notes/r150-nonrankone-execution-789f/20261116-local-original-ten-generator-critical-presentation-v3.json)。

全部数学数组仍只在临时目录。当前完成的是对原全参数 Bell 归一临界理想的准确有限表示，尚未证明该商为零；原非秩一 Bell 根式问题保持开放。
