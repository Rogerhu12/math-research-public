# R80：真实第三桥的完整仿射空间与全相位 P1 的端点障碍

日期：2026-11-14。状态：**已证明**。本文合并 R71、R73、R77、R79，确定指定端口、零二阶矩阵的真实第三桥响应的全部可调空间，再用 R78 把完整第四 $P_1$ 化为两个复模式的同一仿射匹配问题。这里的“完整”指下述有限控制词、时长不受预设上限的桥构造类；不指已完成四阶全部 range，更不指闭嵌入或有限等距族。

## 1. 实际算子空间与端口

固定两个 scalar 常值端芽

$$S_-=(h_-,k_-,\omega_-),\qquad S_+=(h_+,k_+,\omega_+),\qquad h_\pm>0,$$

以及两个指定 frame。真实桥满足

$$h>0,\qquad \omega_s=\frac{k_s}{2h},\qquad F_s=F\Omega(k),\qquad \alpha_s=h^2T.$$

其首末均有开常值 germ；不指定中心线的末位置。所有路径、profile 与恢复使用同一个紧物理区间 $I=[l,r]$、同一个右 collar 和真实右锚。要求全部路径上 $\xi+\omega\geq\delta>0$。**如何在所有辅助控制之间合法固定这个共同 $I$，见第 4 节；此条件不由只检查基准桥代替。**

令 $\mathcal P$ 为共同右 collar 恒零的实光滑 profile 空间。第三响应保留完整的外槽和对称内槽：

$$\mathcal T(f;g,j)=\mathcal T(f;j,g).$$

除非另有证明，不交换外槽与内槽。所有算子等式都是对全部输入 profile、整个 $\xi\in I$ 的函数身份。左尾和更低阶 ruling/period 不因采用右锚而自动支付。

由 R56 的有限分离闭合、R73 的逐点八矩式与 R76 的权分解，本文出现的全部第三算子落在一个固定有限维实空间 $E_3$。这里取**实际函数身份的商空间**，不把某个冗余 primitive 表或其有理代表预设为独立基。

记 R71 的完整三线性交换子空间为

$$W_{71}=\operatorname{span}_{\mathbb R}\left\{[\Phi_i,\Phi_j]:i<j\right\},$$

$$[\Phi_i,\Phi_j](f;g,v)=\Phi_i\bigl(f,\Phi_j(g,v)\bigr)-\Phi_j\bigl(f,\Phi_i(g,v)\bigr).$$

它至多有 28 个生成元，不要求这些生成元独立。记 R77 的完整权三实际可达空间为 $V_3$，R79 的闭水平 C1 实际可达空间为 $W_1$。定义

$$\boxed{W=W_{71}+V_3+W_1\subset E_3.} \tag{1}$$

这三个空间可以有很大的交；本稿不相加它们的形式列数来宣布维数。

## 2. 所有真实零矩桥都有同一个端点类

桥的二阶矩阵总量为零时，R73 的真实第三公式是

$$\mathcal T_B=-\int_B\Phi_{M(s)}\bigl(f,\Phi_{m(s)}(g,j)\bigr)\,ds+\int_B\mathcal C_s(f;g,j)\,ds,\qquad m_s=M,\quad m(0)=m(L)=0. \tag{2}$$

第一项准确属于 $W_{71}$。确切地，写 $M=\sum_i a_iE_i,m=\sum_i m_iE_i$，则 $\int a_im_j=-\int a_jm_i$，因为 $[m_im_j]_0^L=0$；因此历史项是完整三线性交换子的有限实线性组合。没有在分段接缝重置累计 history。

权分解与沿 $h$ 积分给

$$\mathcal C_s=D_s(P_{\rm acc}+P_h)+\mathcal C_{3,\rm rem}+k_sR(h,k,\omega). \tag{3}$$

$P_{\rm acc}$ 为几何速度二次式，在常值端芽的两个端值均零。R77 证明 $\int\mathcal C_{3,\rm rem}\in V_3$，且该空间的任意有限元素真正可达。

对剩余 $R$，R79 给

$$\mathcal H=\partial_h(h^2R_h),\qquad a=R+hR_h,\qquad b=-h^2R_h,\qquad \mathcal K=a_\omega-2b_k,$$

且 $W_1$ 正是 $\mathcal H,\mathcal K$ 全部实际几何系数的跨度。在 $E_3/W_1$ 中，$\bar a,\bar b$ 不依赖 $h$，$\bar a_\omega=2\bar b_k$。固定参考 $(k_*,\omega_*)$，可取

$$\bar F(k,\omega)=\int_{k_*}^k\bar a(v,\omega_*)\,dv+2\int_{\omega_*}^{\omega}\bar b(k,u)\,du. \tag{4}$$

于是 $\bar F_k=\bar a,\bar F_\omega=2\bar b$，沿真实水平路径有

$$\bar R\,dk=d\bar F,\qquad \left[\int_B R\,dk\right]=\bar F(k_+,\omega_+)-\bar F(k_-,\omega_-). \tag{5}$$

从这个商类取任意实际算子代表，连同 (3) 的 $P_h$ 端差，记为

$$\mathcal T_{\rm end}=P_h(S_+)-P_h(S_-)+\text{一个 }\bar F(k_+,\omega_+)-\bar F(k_-,\omega_-)\text{ 的代表}. \tag{6}$$

它只在模 $W_1$、从而模 $W$ 的意义下唯一。更换 $h$ 原函数的锚或势的代表时，必须连同全部补偿端差一起变换。当前 $h=1$ 零锚且两端 $h=1$ 的实例有 $P_h$ 端差准确为零；不能把这项在一般端口也删掉。

由 (2)–(6)，**每座指定端口的真实零矩桥**都满足

$$\boxed{\mathcal T_B\in\mathcal T_{\rm end}+W.} \tag{7}$$

因此 $\mathcal T_{\rm end}$ 不是可无条件设零的“初始化选择”。它记录固定 scalar 端口对真实第三响应施加的仿射约束。

## 3. 反向包含：这正是完整可达集合

**定理 1。** 在第 4 节的共同物理域与有限控制词约定下，指定 scalar/frame 端口、二阶总矩阵 $M=0$ 的实际第三响应集合准确为

$$\boxed{\operatorname{Reach}_3(S_-,S_+;F_-,F_+;M=0)=\mathcal T_{\rm end}+W.} \tag{8}$$

**证明。** 包含方向已由 (7) 给出。R70 首先提供一座真实有限长度的零矩基准桥 $B_0$，准确匹配指定 frame 与 scalar 常值端芽。故存在 $w_0\in W$，使 $\mathcal T_{B_0}=\mathcal T_{\rm end}+w_0$。

给定任意 $w\in W$，按 (1) 写 $w-w_0=w_{71}+v_3+w_1$。R71 的准确交换子词实现 $w_{71}$；R77 的有限真路径基与准确局部参数实现 $v_3$；R79 的闭水平路径族、有限维逆函数定理和有限重复实现 $w_1$。三类都给出真实 $M=0$、frame 恒等、回到相同 scalar 常值 germ 的有限环。它们可在 $B_0$ 的右端常值 germ 处串联，并按实际右端 frame 作同一环境刚体转动。

真实 composition 为

$$\mathcal T_{B_2B_1}(f;g,j)=\mathcal T_{B_1}(f;g,j)+\mathcal T_{B_2}(f;g,j)-\Phi_{M_2}\bigl(f,\Phi_{M_1}(g,j)\bigr). \tag{9}$$

在此每个插入环 $M_i=0$，交叉项准确为零，第三响应严格相加。frame 恒等与同 scalar germ 保持基准桥的两端全部指定条件。最终响应正是 $\mathcal T_{\rm end}+w$。所有重复次数有限，没有以无限极限路径作为实现。证毕。

定理使用的是**完整三线性**控制。仅在对角 $q\mapsto\mathcal T(q;q,q)$ 上成立的一个关系，不能反推 (8) 中某个完整外槽响应；对角映射可以有非零 kernel。

## 4. 物理区间、状态界与时长的量词

上述可达性不是任意受限最优控制问题的解。合法选择顺序是：

1. 固定端口与一座 R70 基准桥；取 R71 的有限交换子控制族、R77 的一个面积 pulse 与四类 step 及其 prefixes、R79 的两类水平闭路字和收缩补偿矩形。所有参数先放在紧小盒中。
2. 把 R70/R72/R76 需要的辅助桥、完整圈数和端点右逆一并选择。在紧参数族上可取固定有限辅助词；必要时用有限覆盖。全部路径于是有某个统一的 $0<h_{\min}\le h\le h_{\max}<\infty$、有限 $|k|,|\omega|$ 界及所需有限阶界。
3. 在这些完整族确定后，选同一个紧 $I$，使全部路径和参数上 $\xi+\omega\ge\delta>0$。随后才在这个固定 $I$ 的实际算子空间上选择 R77/R79 的有限真基与 IFT 子族。
4. 任意有限控制目标超出局部参数范围时，分成有限份、重复同一组小环。每次回到同一 scalar 状态，所以重复增加时长和空间位移，但不扩大已经固定的状态范围或改变右 collar。

因此存在适用于这套构造的统一有限状态界；对有界目标系数族，可统一重复次数和控制词，并获得光滑参数依赖。但本定理**没有证明**下列额外约束下仍有 (8) 的反向包含：

- 任意预先给定、只对原始基准桥物理的 $I$；
- 任意事先限定的 $h,k$ 小盒、几何速度或曲率上界；
- 指定总时长或一个独立于目标的时长上限；
- 指定桥的空间位移、无自交或厚度预算。

若加上这些限制，(7) 仍是必要的代数包含，但可达集合可能严格更小。不能把“每个已构造有限词都各自有界”改写为“任何规定界内均可实现”。

所有算子身份同时适用于选定 $I$ 上的全部右 collar profiles；控制路径不逐个 profile 重新规范 $\omega$。改变后续 profile 支撑时，仍须留在同一个已支付物理区间。插入环一般改变 $\alpha$ 的末位移；在 R45 的完整单 $P$、$P$、倒行 $P$、倒行 $P$ 结构中，使用**同一个修改后的 $P$**仍准确消除这一位移。该组装只处理 frame/scalar/位置闭合，不给嵌入或 reach。

## 5. 两模式的同一仿射障碍

固定 R78 的正负常态 pair、真实长度尺度 $\ell$，令 $\mathcal A=\ell r_+$。先考虑一个 pair；多个 pair 的总响应在本节各式中求和即可，逐 pair 令零是充分选择而非必要条件。

在 $E=\operatorname{Sym}^2\mathcal P$ 上，R78 定义 $\mathcal K,\mathcal L$，并令 $\mathcal Q=\mathcal K-\operatorname{Sym}\mathcal L$。对任意完整第三改变量 $\tau$，其准确线性变化为

$$\Delta\mathcal K(D_1,D_2)=\tau(\mathcal A D_1;D_2)+\tau(\mathcal A D_2;D_1), \tag{10}$$

$$\begin{aligned}
\Delta\mathcal L(x\odot y,D)={}&-2\tau(x;y\odot\mathcal A D)-2\tau(y;x\odot\mathcal A D)\\
&+2\mathcal A\bigl(x,\tau(y;D)\bigr)+2\mathcal A\bigl(y,\tau(x;D)\bigr),
\end{aligned} \tag{11}$$

$$\Delta\mathcal Q=\Delta\mathcal K-\operatorname{Sym}\Delta\mathcal L.$$

取实 $f,g$，$F=f^2,d=f^2-g^2,q=f+ig$。复数使用普通复多线性延拓，不改成 Hermitian 配对。定义联合实线性响应

$$\boxed{\mathfrak B_{f,g}(\tau)=\left(\frac{\Delta\mathcal Q(q^2,q^2)}{16},\ -\frac{\Delta\mathcal L(F,q^2)+\Delta\mathcal Q(d,q^2)}4\right).} \tag{12}$$

它的两个分量分别为 $-4,-2$ 模式的整个复函数，即四个实函数。$\tau$ 的同一组**实系数**同时进入两分量。不得分别求出两套系数后称为同一真实桥。

令 $\mathfrak J_{f,g}$ 为 R78 两个模式中与 $\mathcal T$ 无关的 bulk 局部漂移。把公式中的 $\mathcal T$ 形式地置零只是定义这一常项，不主张存在零第三响应的物理桥。定理 1 给完整可实现的模式集合

$$\boxed{\mathfrak J_{f,g}+\mathfrak B_{f,g}(\mathcal T_{\rm end})+\mathfrak B_{f,g}(W).} \tag{13}$$

相应端点障碍为

$$\boxed{\mathfrak O_{f,g}=\left[\mathfrak J_{f,g}+\mathfrak B_{f,g}(\mathcal T_{\rm end})\right]\quad\text{在实际函数商 }E_{4,f,g}/\mathfrak B_{f,g}(W)\text{ 中}.} \tag{14}$$

这里 $E_{4,f,g}$ 只需取常项和有限控制像的实际实线性跨度。也可不固定 $f,g$，把 (12)–(14) 取为对全部 profiles 的四次算子身份，得到 universal 版本。

**定理 2。** 在定理 1 的构造类中，同一真实桥可使该 pair 的完整 $P_1$ 对所有相位、整个 $I$ 恒零，当且仅当 $\mathfrak O_{f,g}=0$。

**证明。** R78 证明完整相位零恰等价于 (12) 的两个模式均零，其余模式为共轭，常数模式由 $P_1(0)=0$ 决定。定理 1 把允许的 $\mathcal T$ 精确列为 $\mathcal T_{\rm end}+W$，故代入即得必要性。若 (14) 为零，存在一个 $w\in W$ 使 (13) 为零；定理 1 真正实现这个完整 $w$，得到同一桥，给充分性。证毕。

更换端点代表 $\mathcal T_{\rm end}\mapsto\mathcal T_{\rm end}+w_*$ 只把 (13) 的常项平移 $\mathfrak B(w_*)$，不改变障碍类。因此该障碍不依赖打印了哪一个 primitive 代表、选择哪一座真实基准桥，或在哪个合法 $h$ 原函数规范中计算。

## 6. 纯模式阳性所支付的内容

令 $\tau_{\rm diag}(q)=\tau(q;q,q)$，则 (12) 的第一分量也可写为 R71 的

$$\mathfrak B_{-4}(\tau)(q)=\frac18\left\{D\tau_{\rm diag}(q)[\mathcal A(q,q)]-2\mathcal A\bigl(q,\tau_{\rm diag}(q)\bigr)\right\}. \tag{15}$$

因此纯模式可以只消费对角三次资料；第二分量一般不能。R78 给出的非零对称平方型和 R81 的真实非零 hook 控制，均说明丢弃外槽信息会漏掉完整相位条件。

公开 Actions **43632772378**、source `31a276f6f4b2361d10bea9a46fea307a951bb639` 的 `closed_c1_endpoint` 实际输出，已经从原始有锚表达式验证全部 101 个端点几何行，并验证

$$\text{原纯 bulk 目标}+\mathfrak B_{-4}(\mathcal T_{\rm end})+\text{一个可实现控制响应}=0. \tag{16}$$

证据为 [实际报告](../notes/actions-43632772378-1-closed_c1_endpoint/closed-C1-endpoint.json) 与 [准确关系](../notes/actions-43632772378-1-closed_c1_endpoint/closed-C1-endpoint-relations.json)。主报告的 `verified_original_whole_function_identity` 为 true；`all_phase_channels_satisfied` 为 false。本稿不重复该证书的全部有理系数。

(16) 是 (14) 投到纯模式后的真实阳性实例。此前只检验齐次响应空间而遗漏端点常项，不能用那次无关系结果判定这一仿射问题。与此同时，打印的端点代表有 10 项，不构成该端点算子非零或商类非零的独立证明；响应列的代表秩也不自动给实际函数空间维数。完整相位仍须由同一实控制同时支付 (12) 的第二分量。

## 7. 无关系结果怎样成为真正的障碍证书

定理 1 说明，同一允许类中的第三可调方向已经全部包含在 $W$。因此今后的“未找到关系”应区分两个问题：

1. 有声但不完备的 IBP/shuffle 正规化可能还未识别真实函数身份；其非零代表余项或有理矩阵无解，**本身不是** (14) 非零。
2. 若在实际函数空间中证明 (14) 非零，则继续添加同一类零矩第三环不会解决它。此时须改变 bulk/端口/profile 选择或其他构造条件，而非给已在 $W$ 内的同类控制另取名字。

一种不依赖正规化完备性的严格负证书如下。选 $W$ 的一个有限实际生成表 $\tau_1,\ldots,\tau_m$，令

$$v_j=\mathfrak B(\tau_j),\qquad v_0=\mathfrak J+\mathfrak B(\mathcal T_{\rm end}).$$

取有限个**真实函数评价**的实线性泛函 $\Lambda_i$，例如固定 profiles 和 $\xi$ 后取指定模式的实部或虚部。若找到准确实系数 $c_i$，使

$$\sum_i c_i\Lambda_i(v_j)=0\quad(j=1,\ldots,m),\qquad \sum_i c_i\Lambda_i(v_0)\ne0, \tag{17}$$

则 $\Lambda=\sum_i c_i\Lambda_i$ 真正消去全部可达响应，却不消去目标，故 (14) 非零。证明只是对任何假设的 $v_0\in\operatorname{span}\{v_j\}$ 施加 $\Lambda$，不需要假设 primitive 独立。

式 (17) 必须在原始有锚表达式上准确验证。有限实函数空间中的点评价分离非零函数，因此若真实非成员成立，有限组这种评价理论上足够；这不保证某一个预设采样网格或浮点截秩给出证明。

可实施的准确测试输入是公共 collar 外支撑的高正则分段多项式，配合准确有理/代数节点及已明确的常数字段，直接计算有限导数与全部 Volterra 积分。须选择高于全部表达式所需阶数的正则性。若定理只把 $C^\infty$ 作为输入，可用保持 collars 的光滑逼近和这些有限阶算子的连续性传递身份；不以不合法的低正则测试制造假反例。

还必须保持两种范围：

- **同一固定 $(f,g)$ 的不可能性：** 所有 $\Lambda_i$ 使用这一对 profiles，只改变模式或 $\xi$。这样 (17) 排除针对该对 profiles 选择的任意真实桥。
- **普遍算子身份的不可能性：** 可以使用不同 $(f,g)$ 的评价，但同一桥控制系数须同时适用这些输入。这样只排除 universal 桥身份，不能排除某个特殊 profile 圆。若另要求三矩、双 collar 等 admissibility，固定-profile 的证书输入也必须真实满足相应条件；不得拿不满足那些条件的测试排除全部合法特殊圆。

## 8. 范围与下一准确目标

本文已经确定给定端口的完整真实第三仿射类，并给完整 $P_1$ 两模式的必要充分函数商判据。它把“缺少真实控制”与“缺少函数身份证明”分开，也说明为什么真实端点项会把此前齐次无关系问题改成新的准确阳性。

即使 (14) 全部为零，尚未支付 $P_0$、第四逐 $s$ ruling、低阶所需的全部双 collar 条件、更高阶与收敛。控制路径的长度和空间位移也可能很大。本文及当前纯模式证书均没有给出主课题要求的完整闭嵌入、全局 reach、握持或宏观运动结论。

证明来源：[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R78](R78-complete-phase-P1-symmetric-square-conditions.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)。
