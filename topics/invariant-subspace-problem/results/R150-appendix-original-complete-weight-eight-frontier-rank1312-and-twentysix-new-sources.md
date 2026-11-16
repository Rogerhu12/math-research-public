# 完整原权八前沿：秩 1312、二十六条新来源与七十四条完整关系

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 实际完成的结论

在同一合法剩余映射 $p=127,d\mapsto100$ 下，保留全部十二参数、十个原模坐标及十八个原生成元来源。本次完整权八计算实际给出

$$\operatorname{rank}_{\mathbb F_{127}}M_8=1312,
\qquad M_8\text{ 的尺寸为 }17674\times1386.$$

前三组原列构成的完整 $G_8$ 秩恰 1106；再加入全部一百八十条 $y_aN_iY_j$ 后，完整 1286 列前缀秩恰 1286。一百条 $N_iC_\ell$ 中实际保留 26 条、删除 74 条。每条保留或删除表达式均通过全部十个参数坐标及原十八生成元多项式乘回。

因此三十条已付 $N_iY_j$ 的全部权一参数倍数，在 $G_8$ 的常数线性商中仍然独立；一百条新交换子像在这一完整父空间的商中贡献恰 26 维。

这是完整有界来源与有限域模等价结论。它不宣称原五十列模已经稳定，不宣称 Bell 单位理想，也不将有限域来源提升为特征零来源。

## 2. 同一原模型与全部来源

令

$$B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
\quad \operatorname{wt}(y)=1,\quad\operatorname{wt}(w)=2,$$

$$m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4)^{\mathsf T},
\quad \operatorname{wt}(m)=(0,2^5,4^4).$$

原十八生成元列 $A$ 按五个 $u$ 梯度、六个 $w$ 梯度、六个 $y$ 梯度与 $b-1$ 排列，$b=y\cdot w$。原精确身份为

$$m^{\mathsf T}N_i=u_i m^{\mathsf T}-A^{\mathsf T}S_i.$$

六条均值 $Y_j$ 权五、二十条保留交换子 $C_\ell$ 权六、十四条保留交换子 $D_\ell$ 权八。其完整原来源已经由 [五十原种子模等价](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md) 支付。

三十条 $V_{ij}=N_iY_j$ 的权七来源及完整秩 312 见 [首层三十原来源](R150-appendix-original-thirty-mean-images-and-complete-weight-seven-rank312.md)。本次对每条新列

$$W_{i\ell}=N_iC_\ell$$

使用字面的原来源

$$\tau_{i\ell}=u_i\sigma_\ell-S_iC_\ell,
\qquad m^{\mathsf T}C_\ell=A^{\mathsf T}\sigma_\ell,$$

并实际核

$$m^{\mathsf T}W_{i\ell}=A^{\mathsf T}\tau_{i\ell}.$$

程序还完整回读并核了五十条乘法列身份、全部四十条所用父种子的十八源乘回、三十条父 $V_{ij}$ 的十坐标与十八源乘回。原十七梯度与该原坐标系的 Jacobian 运输没有改变。

## 3. 完整权八字典与真实秩

完整输出字典为

$$8007+5\cdot1715+4\cdot273=17674$$

行，即十个模坐标上全部合法权八参数单项式。完整原输入顺序为：

| 原来源 | 完整乘子 | 列数 | 本次真实前缀秩 |
|---|---|---:|---:|
| 六条 $Y_j$ | 全部 92 个权三单项式 | 552 | — |
| 二十条 $C_\ell$ | 全部 27 个权二单项式 | 540 | — |
| 十四条 $D_\ell$ | 常数 | 14 | 1106 |
| 三十条 $V_{ij}$ | 全部六个 $y_a$ | 180 | 1286 |
| 一百条 $N_iC_\ell$ | 常数 | 100 | 1312 |

前 1106 列是完整 $G_8$，其中 $G=B\langle Y,C,D\rangle$。前 1286 列是完整 $G_8+\sum B_1V_{ij}$ 的来源列表；它的秩没有预先假定，而是从实际原行消元后读出。

同一已审 F127 native 先完成 244990 项完整域运算检查和 25 项独立普通标量小矩阵乘回，再处理全部 1386 个原输入。此次发生 538462 次完整主元消去，得到 1312 个单位行和 74 个目标依赖式。所有 17674 输出均保留，未作参数点采样、随机投影或高权删项。

一百条新目标的分类总数为 $26+74=100$。每条依赖式的目标系数严格为一，只用先前真实独立原列。完整 Python 消费者将同一原系数重新作用于十参数坐标和十八来源，两种乘回全部通过。

由于前缀已独立且七十四条关系各自有不同的新目标单位坐标，它们也是此完整 $1386\to F_8$ 映射的全部常数核的一组基：核维数为 $1386-1312=74$。这项完整核结论仅针对本页固定权八矩阵，不将其扩大为原参数模的全部多项式关系。

## 4. 保留二十六条后的完整模等价

记

$$L_0=G+(b-1)B^{10},\qquad
L_1=L_0+\sum_{i,j}B V_{ij},$$

并令 $K$ 为本次实际保留的二十六个 $(i,\ell)$。由每条真实原来源表达式，得到

$$\boxed{
L_1+\sum_{i,\ell}B W_{i\ell}
=L_1+\sum_{(i,\ell)\in K}B W_{i\ell}.
}$$

每次删列均有完整原十八源回填，因此这是整个 $B$ 子模的等式，不只有限维秩相等。反过来，保留二十六条只说明它们在声明的完整权八父空间商中独立；没有据此宣称它们在整个未截断 $L_1$ 中独立。

也不能只由 $N_iC_\ell$ 这一族已经处理就声称稳定：五个 $N_i$ 对其它原生成元及新来源的作用仍需真实来源表达或其它完整证明。任何后继 $e_0$ 正证都必须完成原十坐标、十八源与十七梯度加 Bell 的乘回；特征零恒等须另外验证。

## 5. 不增加计算的完整来源权八推论

沿用 [完整来源权七及 Bell 饱和边界](R150-appendix-complete-bounded-source-weight-seven-and-bell-saturation-boundary.md) 的逐原来源权定义，令 $G_1=G+\sum BV_{ij}$。其不超过八的齐次像是分级直和，实际维数为

$$6+56+312+1286=1660.$$

来源权八允许的 Bell 系数向量是 $F_{\le5}$，其中 $F=B^{10}$ 按原模权分级，并有

$$\dim F_{\le5}=1113+5\cdot126+4\cdot7=1771.$$

若 $(b-1)c\in(G_1)_{\le8}$ 且 $c\in F_{\le5}$，最低权比较先迫 $c$ 的权零至四部分全零；余下 $c=c_5$。再比较权五得 $c_5\in(G_1)_5=G_5$，而 $bc_5\in G_8$ 自动成立。因此准确交空间为

$$ (b-1)F_{\le5}\cap(G_1)_{\le8}=(b-1)G_5,$$

其维数恰为六。故完整来源权八的旧 $L_1$ 像维数为

$$1660+1771-6=3425.$$

加入二十六条新权八方向后，低权及上述六维交空间不变，完整来源权八像维数变成

$$3451.$$

全部不超过八的输出数为 $12713+17674=30387$。这两个有界维数是本次完整秩及分级证明的推论；没有运行另一个 $30387$ 行矩阵。未截断成员性仍允许更高来源权相消，不能由此代替 Bell 饱和的全部幂次条件。

## 6. 两个真实执行阶段

主源为：

~~~text
notes/2026-11-16-r150-original-complete-weight8-frontier127-789f.py
blob 4e8f554b0979ec9c05d0c8c2dfdb024151de3b6b
22828 bytes
SHA256 bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936
~~~

全部精确输入、完整 CLI 与 180 秒 / 768 MiB / 外层 240 秒预算记于同名 `inputs-789f.json` 和 `interface-789f.md`。native 与头文件逐字复用已审版本。

| 真实阶段 | 状态 | 总 elapsed 秒 | 峰值 KiB | raw bytes / SHA-256 |
|---|---|---:|---:|---|
| prepare | exit 0，100 个完整来源及输入 | 102.7196072509978 | 255228 | 46356 / `c56e0a8a5024ec55b428131fbd543ae05b2278792427c95f3bf968cff1169fa1` |
| 同 binding 的 final | exit 0，全部秩与关系终门 | 85.21685763800633 | 父 272028；子 262300 | 73556 / `10c6ba5e961b9b1c06e87589df34ebaadfd227486725b8d4dda0b6a29f439804` |

final 总时间包含父数学回读、编译、native 和全部原乘回；native 数学段为 4.83292 秒。final 复用已经封存的一百个原来源阶段和完整输入，不重新生成它们；实际原产品仍重新验证。

同一主 binding 为：

~~~text
1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069
~~~

| 完整临时对象 | Bytes | SHA-256 |
|---|---:|---|
| 完整 1386 原输入 | 24496256 | `b9c8085459685cdf728e9ba8cbc005daccfc80a0d8047ddccddb008e4002249a` |
| 完整原字典 | 586948 | `4164b25bfaa7504c12cb40d20fa3f9d22887d71b75bae943121808a4fc686ab0` |
| native 完整状态 | 22008128 | `e561e3652a0dd2583c8c6b2206c34f5e1c8b0ab4d77275a35b25f16db5ae581e` |
| native 完整结果 | 113472 | `c866eab92a0aa9a5c451b96135647a6391b9f6dc242b5ae9fa03aa9da54eb36d` |
| final manifest | 73953 | `08254a15dbbf01c44fc53ee4e88d8dfd7b5f8b815ee377dd30167547df6b68d1` |
| 最终来源证书 gzip | 286265 | `dc6a303532c79ec002a35f3020aa4649db6527da34027a518053af458738a2c3` |

来源证书解压逻辑数据为 1839972 bytes / SHA-256 `39acbe100bd7f05adfb393443f06f9d3fce2d43040c63e402af94394503146c3`。全部 201 个完成阶段具有完整物理与逻辑身份。两阶段执行身份分别为

- `notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete-weight8-frontier127-prepare180.json`；
- `notes/r150-original-parameter-module-execution-789f/local-20261116-original-complete-weight8-frontier127-final180.json`。

所有矩阵、系数、完整 raw 和 native 状态只保留在临时目录；仓库保存源码、参数、证明及执行身份/SHA。本页没有启动权十大矩阵，也没有新增任何 Singular 候选或特征零单位来源声明。

## 7. 根的独立完整秩与全核复核

根另以独立二进制读取和 python-flint 普通模矩阵运算，直接消费全部原输入与完整结果；没有调用生产者的消元或来源解析函数。先逐一核完全部 201 阶段的物理/逻辑 SHA 及全部 native 文件，再从字面原输入取出实际 1312 阶子式，其行列式在 $\mathbf F_{127}$ 中为 $4$。这独立支付秩的下界。

随后把全部七十四条完整原核关系组成矩阵，与全部 $1386\times17674$ 原输入相乘，所有 $1,307,876$ 个输出坐标均严格为零，核关系矩阵自身秩为 74。这独立支付秩上界并确认完整核；全部前 1286 个原输入也包含在同一原单位子式中。

审计实际 exit 0，耗时 30.281215362003422 秒，峰值 671804 KiB。审计源码为 [完整原子式与核审计](../notes/2026-11-16-r150-original-weight8-full-rank-and-kernel-audit-789f.py)，5896 bytes / SHA-256 `ce973bb43211fc1ea5993a072364cdeee0c0f66e4ee2583cf164c5dad4164bda`；完整临时 raw 为 966 bytes / SHA-256 `88faee5b544f418b55ea6093d53f54c0370769dbd31d7e996cbf0f2981dda40a`。执行身份保 [根独立审计记录](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-weight8-full-rank-and-kernel-audit.json)。审计未写出矩阵或核数组，也未增加任何特征零、稳定闭包或单位理想断言。
