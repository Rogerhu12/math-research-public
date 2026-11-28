# R150 补充：W/b0 整个正 e 射线排除及 e、k、u 的1009整单位性

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

## 1. 完成结论

在当前正确W、完整b0=0及物理非零图内，不存在剩余特征1009的原赋值满足
$$
v(e)>0,\qquad v(k)=0.
\tag{1}
$$
本稿关闭整个(1)，包括全部lambda/f极点及k的各个剩余中心。最后的一般k唯一中心由完整singleton两原式的单位Bézout排除，不需要选择物理f或假定其根简单。

与五个其他射线的已成证明及既有Newton穷尽性合并，任一当前W/b0原代数点在每个1009位置都满足
$$
\boxed{v(e)=v(k)=0.}
\tag{2}
$$
再用[整个内部u正阶边界排除](R150-appendix-unit211-W-b0-internal-u-positive-entire-original-valuation-exclusion.md)，得到
$$
\boxed{v(u)=0,\qquad u=e+1.}
\tag{3}
$$
这尚未支付Vbar、delta、M等其余原分母，也尚不是整个W空性或完整原整模型。

## 2. 正 e 射线的完整覆盖

原剩余k非零。此前已成结果覆盖下表：

| k剩余范围 | 完整已付结论 |
|---|---|
| k=-2 | [整个k负二原赋值支](R150-appendix-unit211-W-b0-positive-e-k-minus-two-entire-original-valuation-exclusion.md)：正负ell、全部mu极点和唯一有限中心全部排除 |
| k=4且lambda有极点 | [正四中心完整原切锥](R150-appendix-unit211-W-b0-positive-e-k-four-pole-complete-original-tangent-cone-exclusion.md)：全部相对阶覆盖 |
| k=4其余值；k=-4全部值 | [准确q2及正负四原排除](R150-appendix-unit211-W-b0-positive-e-unit-k-exact-residual-quadratic-and-k-plus-minus-four-exclusion.md)，结合原lambda限制 |
| k不等于-2、±4 | [完整五原六元呈示及唯一中心](R150-appendix-unit211-W-b0-positive-e-generic-k-five-original-six-generator-presentation-and-one-residue-center.md)，只余下文(4) |

在最后一行，[原lambda限制](R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)已经迫lambda单位；[完整物理f整性](R150-appendix-unit211-W-b0-positive-e-generic-unit-k-physical-f-integrality-and-singleton-model.md)已经迫f、sigma及全部原Gram坐标整。这两项不能只凭物理非零假定。

唯一剩余中心准确是
$$
\bar L=\frac34,\quad \bar\mu=-2,\quad
\bar\lambda=\frac12,\quad\bar k=-8,
\qquad L=(k+2)/k,\quad\mu=2\lambda-3.
\tag{4}
$$
该中心来自整个一般图的完整五原Bézout，不是为计算挑选的一个模点。

具体地，五原联合已返回剩余标量 $L-3/4$；原完整
$$
q_{\rm raw}=\frac{(3-2L)^3}{9}\mu^2
 -4(3-2L)(L-1)\mu+2(3-2L)^2-3
$$
在L=3/4时为 $3(\mu+2)^2/8$。在剩余域中即迫mu=-2，而没有把全原理想当作约化商。

## 3. 唯一中心的完整两个 singleton 原式

保同一个真实singleton行B，取已经付清的完整首阶必要式
$$
P_0=[P_B]_0,\qquad P_1=[(N_B-P_B)/e]_0.
\tag{5}
$$
原物理右侧 $P_{02}h^3,2\lambda P_{02}h^2$ 都有至少二阶，因为P02有准确e平方因子，且全部物理坐标已整。因此每个原解都在同一剩余f上满足(5)。

(4)给
$$
M_0=1/2,\quad m_0=1/4,\quad T=-1/2,\quad [V_s]_0=-5/2.
$$
原恢复的所有实际分母在此均为1009单位。物理f保持自由；没有f=0、t=0或某一f根的选择。

从完整原Gram得到QQ上的
$$
P_0=48f^3-480f^2+1686f-1944.
\tag{6}
$$
唯一新源从真实双数Gram的一阶定义核回(6)，并形成完整P1。两原式在1009上的实际系数为
$$
\begin{aligned}
p_0(f)&=48f^3+529f^2+677f+74,\\
p_1(f)&=646f^3+5f^2+919f+305.
\end{aligned}
\tag{7}
$$
这两个短三次是完整(5)的剩余；并非两个独立范数的必要根集合。

## 4. 明确的完整原单位身份

唯一预定的新一元Bézout返回
$$
\begin{aligned}
a(f)&=793f^2+234f+749,\\
b(f)&=822f^2+503f+513,
\end{aligned}
$$
以及
$$
\boxed{a(f)p_0(f)+b(f)p_1(f)=1
\quad\hbox{于 }\mathbb F_{1009}[f].}
\tag{8}
$$
程序核全部商余乘回和(8)的所有系数，并用(5)的原QQ两式及乘子提升再次逐系数核模身份。没有只看裸gcd次数。

所以(7)在代数闭剩余域中也没有共同f。它排除了(4)的全部f值及任意更高阶接近。L、mu、f沿原赋值可同时变化；(5)的正则性保证其剩余仍是(7)，无需把实际特征零坐标固定为显示的QQ数。

结合§2的完整覆盖，(1)无原解。

## 5. 从六条射线到全部 e、k 整单位

[已成Newton穷尽性](R150-appendix-unit211-W-b0-three-excluded-1009-Newton-directions-and-six-retained-boundaries.md)由两个完整必要权曲线C74/D78的顶点单位和九个共同边证明：对任何原代数点和任意1009位置，若(v(e),v(k))非零，则其为下表六个向量之一的正倍数。该论证保任意代数闭剩余扩张；本稿只静读复用，没有重新运行边gcd或旧两曲线门。

| 方向 | 原完整排除 |
|---|---|
| (-1,0) | [负e射线](R150-appendix-unit211-W-b0-negative-e-ray-complete-q2-R6-valuation-exclusion.md) |
| (-1,1) | [负e正k整对角](R150-appendix-unit211-W-b0-negative-e-positive-k-entire-diagonal-ray-exclusion.md) |
| (0,-1) | [整个负k射线](R150-appendix-unit211-W-b0-entire-negative-k-ray-original-q2-R6-N5-exclusion.md) |
| (0,1) | [一般正k两中心](R150-appendix-unit211-W-b0-positive-k-ray-only-e-plus-minus-one-original-centers.md)、[e正一中心](R150-appendix-unit211-W-b0-positive-k-e-one-center-original-D-over-M-exclusion.md)、[e负一整中心](R150-appendix-unit211-W-b0-positive-k-e-minus-one-complete-original-valuation-exclusion.md) |
| (1,-1) | [正e负k整对角](R150-appendix-unit211-W-b0-positive-e-negative-k-entire-diagonal-ray-exclusion.md) |
| (1,0) | 本稿§2—4 |

因此没有非零方向，得到(2)。e为整单位使u=e+1整，故v(u)不可能负；其正阶又被整内部u边界原证明排除，得到(3)。

这仅在指定1009位置证明三个实际权坐标为单位。Vbar、delta及其他原权分母仍可能为正阶，原lambda、f等其余坐标在那些边界的行为仍须按原式处理。不能把(2)—(3)直接替换成完整原局部化的有限自由模型或Nakayama空性结论。

## 6. 唯一实际执行与保存

[新唯一中心源](../notes/2026-11-29-unit211-W-positive-e-generic-k-only-L-three-quarter-mu-minus-two-singleton-input-8542.py)，
blob **4208d1e323092fc89fcd82dec968e414d28875b1**，SHA
**b52207ee0e92a63056bdf26007c7471eb8b164580cf66b74e34524b8f4e4cc60**。

[事前固定输入](../notes/2026-11-29-unit211-W-positive-e-generic-k-only-L-three-quarter-mu-minus-two-singleton-input-8542-input.md)只约定一个原式对和固定1009。

唯一[run46177571185](https://github.com/Rogerhu12/math-research-public/actions/runs/46177571185)，job141079641729：

- 固定30秒/256MiB，外45秒；实际 **0.0890012070000239秒 / 39412KiB / exit0**。
- 全部两数学记录亲读，最后数学阶段0.04973086499995816秒；两个新中心原返回、四次有限域商余、一次完整Bézout完成。
- stdout **1773B**，SHA **99ad5a98995710d8ef177f239f03e4a9e3ec2c96bef36500eccbb9eec995f277**；重组原行与driver完全相符。
- source commit **a3c12beb685a101f99c112f1a6ac1b330636a751**；实际pull **5975dfb4c04f5d5e1b7c384696cf63dfc8bd2bcb**，UTC **2026-11-28 18:45:45.456792**，两README无变。

唯一必要定义依赖仍是2f951首阶源的4750B前缀，SHA
ce658823d68f6afba617d80088f5073fcccb79a3550509bce4b220f7a8d8f3b8。
仅在定义层代入已由整图强迫的(4)；AST不执行旧顶层断言、旧四原循环、旧f结式或新已成18列。没有任何旧冻结目标的复算。

[小回执](../notes/2026-11-29-unit211-W-positive-e-generic-k-only-L-three-quarter-mu-minus-two-singleton-input-8542-execution.json)保存两条实际记录及(7)—(8)短原身份。整个W、其余内部DVR边界与普通ISP仍未完成。
