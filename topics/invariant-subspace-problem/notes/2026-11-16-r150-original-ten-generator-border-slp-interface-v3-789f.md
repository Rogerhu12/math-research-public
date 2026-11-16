# 原十生成元的完整乘法来源及有限临界 presentation

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

## 固定输入与入口

全部输入绑定见同目录的
2026-11-16-r150-original-ten-generator-border-slp-inputs-v3-789f.json。
只读既有原十二 NF、十一常二次、六 mean、16条已核三次来源。Python-flint 0.9.0。

~~~sh
python 2026-11-16-r150-original-ten-generator-border-slp-and-critical-presentation-v3-789f.py \
  --low-out LOW_OUT --leading-out LEADING_OUT --six-out SIX_OUT \
  --candidate-out CANDIDATE_OUT --verified-out VERIFIED_OUT \
  --out OUT --seconds 180 --memory-mib 4096
~~~

每个实际父文件的压缩 SHA、逻辑 SHA、binding 均核。六个大 mean 文件不整读：
先逐块核完整两个 SHA，再逐 JSON monomial/coefficient pair 读取并核原18变量支持和权重。
输出亦以 json.dump 逐块编码至 gzip，同时计算完整逻辑 SHA。

前两版各有真实 exit137，均无完整最终回执或 presentation，不能冒作完成。
v3 仅改变共享图、读取和封存策略；全部原来源、常逆、lower系数与数学公式保持。

## 精确算术图语义

图的常数域为原匹配 E；参数为 y6,w6，普通变量为 u5。
节点是整数、原固定 E 引用、原参数多项式引用、变量、加法及乘法。没有参数倒数。
每条边指向更早节点，完整 nodeWeights 和 nodeUDegreeUpperBounds 随图保存。

originalConstantE 引用的值有两种已核编码：三个有理字符串表示 $(1,d,d^2)$ 的系数；
或原18变量 monomial/coefficient 列表，但其支持已核仅在 $d^0,d^1,d^2$。
originalParameterPolynomial 使用原完整18变量列表，已核其中无 u 变量。
这只是原数据的精确引用；绝不是数值采样或截断多项式。

有理恒等式依照已核原 top 来源及逐式通用代入证明。回执明确区分
allParameterIdentitiesCertifiedByExactUniversalSubstitution 与
expandedParameterCoefficientProductsClaimed:false；它不声称展开过全部巨大参数系数乘积。

## 输出及完整来源

两个临时输出：

- complete-original-ten-generator-border-arithmetic-dag.json.gz；
- complete-original-ten-generator-critical-presentation.json.gz。

完整 basis 为 $m=(1,u_0,\ldots,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4)$。
五个 $N_i$ 及五个11×10来源矩阵 $S_i$ 满足
$$
u_i m=mN_i+(F_5,G_w{}_6)S_i.
$$
全部50条来源已回到实际 du5,dw6，不停在 NFdw 的中间坐标。

还保存100条完整交换子及原来源：
$$
m(N_iN_j-N_jN_i)
=(F_5,G_w{}_6)(S_jN_i+u_jS_i-S_iN_j-u_iS_j).
$$
这不表示 $N_i$ 在自由10模上可交换。

有限 presentation 是 $E[y,w,u]$ 上10×68矩阵，列依次为：

1. 全部50个 $u_iI-N_i$ 列；
2. 全部11个 $G_g(u)e_0$；
3. 六条原 mean 的十坐标向量；
4. $(y\cdot w-1)e_0$。

原完整来源顺序为 du5、dw6、dy6、Bell−1，共18项。
50列、11列、6列和最后1列各自的18坐标来源全保留。

九条字面循环路径给 $e_b=m_b(u)e_0$。因此该 presentation 循环，11个矩梯度、
六个 mean 和 Bell−1 均杀 $e_0$；反向以 $e_b\mapsto m_b$ 利用全部原来源定义映射。
两映射逐 $e_0,e_b$ 互逆，故 cokernel 恰为原 Bell 归一临界商。

没有要求自由10上的交换，没有宣称10步稳定，也没有删参数关系或判该商为空。
全部 Bell=1 的6/7局部生成结论仍须按实际子式开集处理，不由泛点代全参数。

## 精确57列子集

实际模型完整保存68列。取零起始列 $0,\ldots,49,61,\ldots,67$ 即为完整10×57表示。
若 $R_{i,a}=u_i e_a-N_i e_a$，则普通二次系数给
$$
G_g(u)e_0
=\sum_{i\le j}q_{g,ij}(R_{i,u_j}+u_iR_{j,0})
+\sum_jL_{gj}R_{j,0}.
$$
余向量严格由原常逆 $UD=I$ 为零。因此删去的11列已有明确原来源，没有新参数逆或稳定迭代。
57列全部对 u 至多一次。这是同一实际输出的数学推论，不另称执行已产出57列文件。
