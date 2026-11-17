# R640：实际 pulse 开放前缀的连续圆柱图嵌入证书

2026-11-17，geometry_amplification。**已证明的应用范围：** 对固定 binary 共同节点及0/1/2jet定义的字面 M320 场，在与R638相同的标准 IEEE binary64 向外舍入模型下，下列区间证书封闭全部径向位置和全部角度。因此由既有 [R9](R9-cylindrical-graph-global-embedding.md)，该**未规范化**映射 `F:[0,1]×S¹→R³` 是带边 C² 嵌入。没有重发R9的一般定理，也没有把该结论转给随s缩放后的规范化图G。

## 1. 固定字面对象和结论

输入为完整旧前缀与 A=−5、w=.005 pulse 桥拼接的
`parallel-pulse-a5-complete-base.json.gz`，SHA256
`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。
其818胞元都使用保存的实际两端0/1/2jet，逐胞元取唯一Hermite五次式。依次拼接 x/Y/D/DD 的 little-endian float64 身份为
`840193a1cdb37f79d04f5f36f5a0c485c4eb50f3fd2a103af8c4c267d5232793`，与 [R638](R638-global-positive-arclength-coordinates-for-two-prefixes.md) 相同。此处节点及jet解释为精确实数的二进制数据，不把其生产ODE或标量Gauss求积当准确解。

写真实映射为
\[
 F(s,\phi)=\operatorname{Rot}_\phi(R(s,\phi),T(s,\phi),Z(s,\phi)),
\]
其中R/Z为偶余弦、T为奇正弦，最高频2M=640。所有胞元共享两jet，故该有限角谱映射为C²。

令 d、V 分别为实际 `Fφ,Fs` 在旋转坐标中的分量，定义
\[
 Q=R^2+T^2,\quad A=R d_T-T d_R,\quad B=R V_T-T V_R,
 \qquad C=V_Z A-d_Z B.
\]

本次全域向外计算给出：

| 量 | 整个连续域的下界 | 最差胞 |
|---|---:|---|
| Q | ≥.1872984476414501 | [0,.00015625] |
| A | ≥.17702008298379882 | [.9999843749999884,1] |
| C | ≥.05100656378603818 | 同上 |

可直接使用保守有理表述 **Q>.1872、A>.1770、C>.0510**。它们不是有限网格上的最小值。

core的degree1由准确有理半平面界支付：
\[
 R(0,\phi)\ge R_0-\sum_{m\ge1}|R_m|
 =\frac{4497374209891218952473871339}{9903520314283042199192993792}>0.
\]
所以 `R+iT` 在右半平面，`β=φ+arg(R+iT)` 一次绕轴。全域Q>0保持这个同伦度数。再由
\[
 \beta_\phi=A/Q>0,\qquad
 \beta_\phi Z_s-\beta_s Z_\phi=C/Q>0,
\]
R9的全部条件已付：在固定β下高度严格按s排序，故F是整个紧环带的C²嵌入。此结论只依赖已固定的几何多项式与三项正性，**不使用标量a(s)的数值积分误差假设**。

## 2. 径向全部位置的覆盖

在宽h的胞元，以归一变量u表示完整系数向量。其六个Bernstein控制向量准确为
\[
\begin{aligned}
b_0&=y_0,&b_1&=y_0+hv_0/5,&b_2&=y_0+2hv_0/5+h^2a_0/20,\\
b_3&=y_1-2hv_1/5+h^2a_1/20,&b_4&=y_1-hv_1/5,&b_5&=y_1.
\end{aligned}
\]
Fs的四次控制向量为 `5(b[j+1]−b[j])/h`。按标准的 `j/5,(5−j)/5` 权重提升到五次，使位置、物理角导数与Fs都用同一六控制向量形式。

对每个角网格点，冻结区间变换包围这些控制向量的实际三角值。用两次向外de Casteljau二分，得到四个闭径向子胞。每个分量在子胞的全部位置都位于其六控制值的区间凸包；直接对这些分量区间形成Q/A/B/C。因此这里的径向覆盖是整个子胞的盒包围，不是对子胞取有限s样本。

## 3. 全角覆盖与舍入责任

采用2048个等分角。所有被变换的线性分量只有最高频640，低于该网格Nyquist；Q/A/C在网格上由向外区间乘积直接形成，没有把高频乘积截断或插值。尤其C可含角频1920；下面的全角导数余项负责网格间隙，不能以“网格足够多”替代。

令 e=Fφφ、dV=Fsφ，均在同一旋转坐标表达。准确恒等式为
\[
\begin{aligned}
Q_\phi&=2R d_R+2T d_T,\\
A_\phi&=R e_T-T e_R,\\
B_\phi&=d_RV_T-d_TV_R+R(dV)_T-T(dV)_R,\\
C_\phi&=(dV)_Z A+V_ZA_\phi-e_ZB-d_ZB_\phi.
\end{aligned}
\]
对每个分量，六个Bernstein控制向量的 Fourier 系数l1界的最大值控制整个径向胞和全角。以这些分量界逐项支付上式的乘积，得到每胞导数上界L。任一角距最近网格点至多π/2048，所以从该子胞的向下网格下界减去向上的 `πL/2048`，即可封闭全部角度。

最差Q胞的径向盒网格下界为.20622385586849773、角向扣量≤.0189254082270476。最差A/C子胞对应为

| 量 | 径向盒网格下界 | 全角扣量 |
|---|---:|---:|
| A | .28058450314153777 | ≤.10356442015773892 |
| C | .2800084367841406 | ≤.22900187299810243 |

全部胞的最大角导数上界为20.49114336、67.51350537、149.28601115；各胞使用自己的界，而非错误地混用抽样导数。区间变换最大宽度≤1.214e−9，远小于最后的正余量。

新源复用R638的冻结 f512 区间工具：所有算术逐次nextafter向外，正和逐项向上；Machin有理π和整数Taylor角因子、区间radix-two变换的论证直接沿用R638 §3。新层的Hermite控制向量、degree elevation、角系数l1、de Casteljau、乘积和角扣量也全部向外。普通浮点FFT没有进入证书。

`numerical_route` 独立只读审核了新源的Q/A/C角导数、degree elevation和闭子胞覆盖，未另重审已经冻结的f512基础。两个针对性解析核验是椭圆柱 `(2cosφ,sinφ,s)`（准确最小Q=1、A=C=2）以及在core产生 `C=1−2sin²(2φ)` 的反例；前者证书正、后者拒绝。它们检查实现接口，不代替上述全818胞的实际区间运行。

## 4. 冻结复现和未付范围

[全域区间源](../notes/2026-11-17-parallel-geometry-cylindrical-graph-interval.py) SHA256
`d984f0ce6c4622d907f19ed03753e4cc55ee3566a82d1b047c59774c95a08218`。
其已冻结区间依赖 [f512源](../scripts/parallel_20261117_arclength_interval_positive.py) SHA256
`f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。
前置实际读者SHA为 `084a25dee60a3369a41b205be524ba4de197a4097ccf3de49dd3cf13d2f01f15`，不作为本次连续正性的替代。

全部区间报告 `parallel-pulse-a5-cylindrical-graph-interval.json` 保留在仓库外，SHA256
`edef53a99654c73bd7ccc286b60490e17818ce2ab89aaafe9269cb62212d38ca`。复现：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python "$TOPIC/notes/2026-11-17-parallel-geometry-cylindrical-graph-interval.py" --topic "$TOPIC" --input "$SCRATCH/parallel-pulse-a5-complete-base.json.gz" --out "$SCRATCH/parallel-pulse-a5-cylindrical-graph-interval.json" --angles 2048 --radial-subdivisions 4
```

规范化的像 `G=c+λ(F−c)` 还需要λ、λ′的连续预算；R638已付的角坐标微分同胚本身不省去该缩放责任。本条没有升级G、Gram/曲率采样、reach、固定帽、闭合或课题完成标准。
