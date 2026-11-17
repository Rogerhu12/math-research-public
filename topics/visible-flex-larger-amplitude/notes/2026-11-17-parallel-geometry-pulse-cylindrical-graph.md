# 完整 pulse 前缀的圆柱图有限可行性

2026-11-17，geometry_amplification。**实际有限读数；全域连续嵌入条件尚未封闭。** 一般圆柱图嵌入、degree1同伦保持和镜像结论已有 [R9](../results/R9-cylindrical-graph-global-embedding.md)，本条不重发该定理，只给同一个完整实际前缀的新输入。

对象为 `parallel-pulse-a5-complete-base.json.gz`，SHA `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`：原 d6441e 前缀与真实 A=−5、w=.005 局部桥共同六jet拼成的818胞元、M320场，区间 `[0,1]`。这是弧长规范化之前的字面共同quintic图，不擅自代称规范化后的图。

**后续同场结论：** [R640](../results/R640-certified-cylindrical-embedding-of-the-pulse-prefix.md)已在相同26e53e8字面场上严格封闭全部818胞的Q/A/C正性，并由R9给出未规范化前缀的C²嵌入。以下保留此前有限读数的原范围；规范化缩放图另付。

## 实际不变量和严格条件接口

在旋转坐标写 F=(R,T,Z)，实际物理角导数为 `d=(Rφ−T,Tφ+R,Zφ)`，真实径向导数为 V。取

\[
 Q=R^2+T^2,\quad A=R d_y-T d_x,\quad B=R V_y-T V_x,
 \qquad C=V_zA-d_zB.
\]

则真实方位角 β 满足 `βφ=A/Q, βs=B/Q`，R9 的圆柱投影Jacobian为 `J=C/Q`，固定β的高度导数为 `C/A`。全部量由实际保存的0/1/2jet唯一确定的五次场及其字面导数读取；没有以PDE预测替换导数。

若今后在整个连续紧参数域证明 **Q>0、A>0、C>0**，则Q>0将core的degree1沿s同伦传播；A>0令每圈方位映射为圆周微分同胚。固定方位β时 `dZ/ds=C/A>0`，故相同(β,z)强制同一s，再强制同一φ。R9据此给整个带边前缀C²嵌入。这里只是把既有证明绑定到本字面对象，尚未把采样正性替换成这些连续假设。

core度数本身已能准确支付：将存储二进制系数视作精确有理数，

\[
 R(0,\phi)\ge R_0-\sum_{m=1}^{320}|R_m|
 =\frac{4497374209891218952473871339}{9903520314283042199192993792}
 >.4541187443.
\]

因此 R+iT 在右半平面，`β=φ+arg(R+iT)` 的degree准确为1。这不替代整段Q>0的连续门。

## 有限真读数

8192角、每胞元4子分；每胞元包含两端，共33,505,280样点。

| 量 | 最小样本值 |
|---|---:|
| Q=rxy² | .206223855869 |
| R | .454118768461 |
| A | .234769948898 |
| C | .234769948898 |
| βφ | .117400542741 |
| J | .117400542741 |
| 固定方位高度导数 C/A | .545221809279 |
| 普通 Zs | .545221809279 |

前六项最小在core；C/A最小在s=.956875、φ=π/2。R9后续定量弦距所需的 `|Zβ|=|Zφ/βφ|` 最大样本为.176026006625；`|βs|`最大为.345161386882。有限六jet还给 `|As|,|Aφ|,|Cs|,|Cφ|` 的最大样本为6.16989、11.87705、16.63233、9.58224，均未冒称全域导数界。

无分母多项式适合后续连续封闭：Q/A每cell径向次数≤10、C≤14；角频最高分别4M=1280、6M=1920。可在同一系数定义上做径向Bernstein与角区间界。这里没有另起大规模证书，也没有做新点云reach扫描。

## 冻结复现与边界

[读者源](2026-11-17-parallel-geometry-cylindrical-graph-readout.py) SHA `084a25dee60a3369a41b205be524ba4de197a4097ccf3de49dd3cf13d2f01f15`；仅使用既有Frenet有限角jet，其源SHA `7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831`。外部报告 `parallel-pulse-a5-cylindrical-graph.json` SHA `4278bebb2749b1b276f53089e4d5ef5a8117011eb78041a9a85ef2edb49a582c`，保留逐胞元样本极值及梯度。

设 `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`，运行源并传 `--topic TOPIC --input RAW --out REPORT --angles 8192 --radial-subdivisions 4`。RAW为上述26e53e8场，输出不入库。当前没有全域连续单射证书、闭面、reach或课题完成结论；规范化图和更远hold前缀须分别绑定其真实定义后读取。
