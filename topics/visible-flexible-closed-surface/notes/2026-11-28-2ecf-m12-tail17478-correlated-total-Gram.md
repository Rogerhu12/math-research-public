# 原尾源17478完整单元：真实V+W相关Gram严格低于原求解容差

日期2026-11-28；Astra-visible-flex-2ecfcd69-20261128。

本条对G12真实保存场 `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`，完整消费原有限尾source span17478的全部径向点和全部角度。新的连续相对metric上界为

`4810968655513822895/4951760157141521099596496896`

即约9.715673826761085e−10，严格小于原B=2e−9。该原源单元跨两个实际W knot片，两片分别全部认证。它在旧有限峰附近；当前G12微窗最大样本实际在17479，不把17478改称当前唯一最坏单元。

这里只证明一个明确原源单元，未覆盖其余有限尾、有限内端到真cuff的闭合段或完整prefix；没有README完成声明。

## 1. 原源系数准确恢复，没有拟合或换源

原manifest SHA `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104` 的24个raw gzip全部逐bytes、SHA256及Git blob SHA1核对，共18552个准确归一化径向增量，所有相邻块共享节点逐值相同，准确累计抵达原outer cut。

原source在各片以Vr的四次Bernstein表示定义V的五次积分，141个角系数全部保留。累计左值使用原准确二进有理数及原归一化beta：

`V_left=V_initial+beta*S1/30+beta^2*S2/60`，

`S1 += ell*(7*(f0+f1)+16*mid)`，`S2 += ell^2*(s0-s1)`。

这里f0/f1是原Vr端值，s0/s1是原Vrr端值，mid是原Vr中值，真实片宽为beta*ell。没有使用旧近似position重拟合原积分常数。每片Vr五个控制数为

`[f0, f0+L*s0/4, (16*mid-5*(f0+f1)-L*(s0-s1))/6, f1-L*s1/4, f1]`；

V由准确积分得到，Vrr由准确微分得到。全24块核对和本选中片的准确系数恢复自然exit0，59.370768491秒；输出只在scratch，不提交原始数组。

该片准确半径端点为：

- `128073224280328932797352225770664886361995/249469414795428236558929209782889781133312`；
- `640424188066360732082850131363090141732279/1247347073977141182794646048914448905666560`。

## 2. 同一个完整Gram中保留全部抵消

使用原common单位坐标z，T=S+h，h=c−cuff，t=(Tz−S)/h，

`r(z)=c−hR(t)`，`k=r_z=−T R'(t)`。

R是原固定五次图；S保原exact-root严格区间。R'的degree4 Bernstein控制数为

`[k0, k0−21/100, 321/100−2*k0, 1, 1]`，其中k0=2/sqrt(5)。

它们严格位于(.68,1.43)，所以r严格递减；反解仅用此单调性和向外残差包根。首实现的单次binary64 hull转换另外向外加2^-48；上述严格控制范围保证此余量大于转换误差，不把浮点提议当准确根。所得z外包再按保存W的准确二进knots切开。

真实材料角u(theta)和J=|gamma'(theta)|、真实平均弧长a来自原中心曲线。共享消费者用完整小缺陷Fourier展开、明确uniform余项和J/a的准确高阶导数；证明详见同日[完整prefix16总Gram](2026-11-28-2ecf-m12-prefix16-correlated-total-Gram.md)第2、4、5节。u没有被u0替代。

令旋转背景的一阶为

`Br=(cos u,sin u,−w)`，`Bu=(−r sin u,r cos u,0)`。

原V的height Fourier符号沿TailQueries.apply取负，真实W的height符号按保存场取正。以原V和真实W完整一阶构造

`A=Vr+Wz/k`，`B=Vu+(a/J)Wtheta`。

于是实际Y一阶是Yr=Br+A、Yu=Bu+B，而原目标为diag(1+w²,r²)。在取绝对值之前直接形成

`Nrr=2 Br·A+A·A`，

`Nru=Br·B+A·Bu+A·B`，

`Nuu=2 Bu·B+B·B`。

这些是完整非线性Gram的准确分子，包含V/V、V/W、W/W全部交叉项。背景自身的Gram已用准确恒等式抵消，不添加旧统一d0，也不先把V和W各自取范数。V(r(z),u(theta))按原准确多项式评价；W通过保存的完整重复knots及全部146角通道逐段de Boor评价，准确微分系数给Wz，两端六个零约束行确实恢复。

相对误差三分量分别为Nrr/(1+w²)、Nru/(r sqrt(1+w²))、Nuu/r²。本条使用真实1+w²≥1和真实r≥该片左端的保守分母界；没有以背景近似值缩小分母。

## 3. 背景近似只作为有明确uniform余项的计算工具

原Background从既有stable depth4准确primitive和原校准表提议三次x(r)。将它代回已证r(x)原始函数，得到真实径向残差delta_r；原全域|w_r|<24于是支付24*delta_r。

在该片对应原背景profile(0,5)内，原source八阶区间Taylor包w(x)，再代入提议x(r)，得到21次w_app(r)与统一误差epsilon_w。本片delta_r≤2.1298071877705678e−11，epsilon_w严格上界为

`5062221300556300303/9903520314283042199192993792`。

这个近似没有改原背景或目标。只在上述已经抵消的分子中临时用w_app；真值误差准确为

`|Delta Nrr|≤2 epsilon_w |A_z|`，`|Delta Nru|≤epsilon_w |B_z|`，`Delta Nuu=0`。

统一余差不被微分。A_z、B_z在相同真实径向/角盒上向外包；完整背景影响因而已支付，不能把小点误差当成未知高阶导数界。

## 4. 全径向、全角的实际连续认证

每个实际W knot片在两变量上仿射化，采用径6/角10个Chebyshev根；完整节点总Gram先DCT再取系数l1。高阶真实区间Jet给两维全部插值余项，取两个合法tensor telescoping界的较小者。此处使用完整[0,2pi]上的128个角盒，并未借只测少量角度的结论。

全部r逆图不确定性用z外包覆盖。V和w_app在外包上用相同原片多项式延拓；结论只用于原source片与该W片的真实交集。外包中的额外点只扩大预算，不误用另一物理分支。两个准确W片覆盖整个原径向单元，端点由原C2一致性保留。

| 实际W knot span | 最终完整相对metric上界展示 |
|---|---:|
| 217 | 9.715673826761085e−10 |
| 220 | 9.535876e−10以内 |

实际完整自然exit0，61.083520152秒。节点宽度、各分子的DCT界、完整插值余项、背景uniform误差各自存入报告，不只保成功flag。位移/曲率/全时reach仍使用G12自身已发表全曲面证书，本条没有替代或更新它们。

本首消费者初始化共享Central时，epp辅助参数少了8倍；该量只构造本消费者从未调用的central second trace。此次实际路径仅调用u/speed/a，它们全部只依赖准确gamma、e0及已证mean，e0已是正确8*原warp。因而本条已消费的Gram与相位没有受该未用辅助量影响；这份冻结入口不能拿去消费prefix的C二阶匹配。后继全域入口会显式规范该参数。

## 5. 实际身份、重生和范围

| 输入/输出或实现 | SHA256 |
|---|---|
| 准确原源选片producer | `50428fdad075ee4f203fcc87b2fc6e413a8074bd6ba685130ee1c4cf0f30a76e` |
| 全24块核回的选片数据 | `afcdc718c15b1e8ce0c747710f810753c01019074218e0aab431b885099d3c17` |
| 实际总Gram入口 | `d78cf29bbdbadc21c2d03ace980c4449e2743105665de0b2966227d325c8512f` |
| 本次实际区间/Jet核 | `bad372bdf8e1f3db5b12764fd0705ec7dd5d9c6561086cebb772bc301468f34b` |
| 本次原中央arclength核 | `a12b0951e0530c1e359c40f229c6471d306f1369ee3a38c92a780fc7a06e908d` |
| 完整局部报告 | `1f4b5ffa08bba62b287d108160e25584eb5fd656a8477584c6e36f23837fcf60` |
| 原stable depth4 primitive | `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9` |
| 原背景校准表 | `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4` |

场/grid/result/R226/data身份与同日G12实际场note完全相同。首消费者的三个实际文件冻结在公开scripts的 `2ecf-m12-first-tail-correlated/` 子目录，相对加载关系不变；不拿后续优化文件SHA替换这份已实际执行的身份。

S为公开scripts目录，W为按G12实际场note重生的工作目录，R为已核原24 blobs目录，P为上述原primitive，O为新输出目录。先准确重建原选片，再消费同一真实field：

```bash
python "$S/2ecf-m12-exact-tail-selected-span.py" --scripts "$S" --raw-cache "$R" --spans 17478 --out "$O/exact-span17478.json"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python "$S/2ecf-m12-first-tail-correlated/m12-tail-total-gram-local.py" --scripts "$S" --data "$W/m12-prefix-data.npz.gz" --grid "$W/h2-c2-m48-g12-04/grid.json" --field "$W/h2-c2-m48-g12-04r1/result.json.field.npz" --result "$W/h2-c2-m48-g12-04r1/result.json" --correction-bounds "$W/h2-c2-m48-g12-04r1/correction-bounds.json" --source-polynomials "$O/exact-span17478.json" --primitive "$P" --angular 128 --radial-order 6 --angular-order 10 --out "$O/tail17478-total-Gram.json"
```

全部路径可变；准确输入身份和所有原物理参数固定。只源码、此证明和哈希提交；准确选片数组/完整JSON留临时工作目录。后继处理全部原源片、原cap分支、有限内端闭合段及全prefix；局部成功不当整曲面成功。
