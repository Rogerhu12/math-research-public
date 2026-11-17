# 同14个真实轴点的 β=1/4 加权支持

2026-11-17，constructive_model。**已证明的有限范围：** 对普通支持探针中的同14个实际 $G$ 轴点，取固定 $A_\beta=\operatorname{diag}(1,1,1/4)$、中心0、原外向法向，全部满足

$$(A_\beta G)\cdot n>0.3193.$$

最小实际下界为 `0.3193783136539974`，位于 $s=.95,\phi=\pi/2$。没有读取新的场点、没有重新求比例函数、没有改变曲面。此结论还不是全域支持、闭面或reach证书；普通支持为负的事实保持，它与本条的新加权函数不同。

## 1. 直接复用的实际数据

输入是同 `26e53e8c...` 的已完成14点有理表 `parallel-model-pulse-axis-support-probe.json`，SHA256
`828ad538cae8b9e44076246705533bc44e285854ccbead67d3277f0aba9cbfbe`。
每行已有准确 $R,Z,R_s,Z_s,c,c_s,d_T$，以及来自R648全域报告的严格 $|\lambda-1|\le\epsilon$、$|\lambda_s|\le\epsilon_1$ 的逐片来源SHA。轴上 $R,d_T>0$，法向为 $G_\phi\times G_s$。

固定原同场 $G_R=\lambda R$、$G_Z=c+\lambda(Z-c)$，其轴点单位支持等于

$$\frac{D_{\beta,G}}{|G_s|},\qquad
D_{\beta,G}=G_R G_{Z,s}-\beta G_ZG_{R,s}.$$

令 $D_\beta=RZ_s-\beta ZR_s$、$l=\lambda_s$。直接展开，准确有

$$\boxed{D_{\beta,G}=\lambda^2D_\beta
 +\lambda(1-\lambda)(Rc_s-\beta cR_s)
 +lR\{(1-\beta)\lambda(Z-c)-\beta c\}.}$$

因此对于 $0\le\beta\le1$，可取

$$\begin{aligned}
E_\beta={}&(2\epsilon+\epsilon^2)|D_\beta|
 +(1+\epsilon)\epsilon|Rc_s-\beta cR_s|\\
&+\epsilon_1|R|\{(1-\beta)(1+\epsilon)|Z-c|+\beta|c|\},
\end{aligned}$$

得到 $D_\beta-E_\beta\le D_{\beta,G}\le D_\beta+E_\beta$。全部量使用准确有理运算。原探针已给真实 $|G_s|$ 的向上有理平方根包围；再除这个正上界并向下舍入，得到单位支持下界。没有把 $G_s$ 默认设成单位速度。

## 2. 实际下界

| s | $\phi=\pi/2$ 的加权单位支持严格下界（向下取整） |
|---|---:|
| 0 | .454118 |
| .5 | .444878 |
| .8 | .385312 |
| .95 | .319378 |
| .99 | .392783 |
| .995 | .405463 |
| 1 | .405459 |

另一轴的7点下界全部大于1.414。所有数都来自同一次固定 β=1/4 的纯数据复用；没有继续扫描 β 或选择新的场。

## 3. 来源与剩余范围

冻结小源 `parallel-model-weighted-axis-support.py`，3026B，SHA256
`933900cf23f67fb82a358c16b8cede3776a4416796492e94ce2a613065daaad8`。
实际输出 `parallel-model-pulse-weighted-axis-support.json`，SHA256
`338aaee8e87caf070786316082b4690cf31a8c6fd0fb3c60a3ef36d7c6a40f72`。
入口明确记录 `new_field_samples=0`、`new_lambda_evaluations=0`；它只消费原14点表和已付每片预算。

```sh
PYTHONDONTWRITEBYTECODE=1 python "$WORK/parallel-model-weighted-axis-support.py" \
 --axis-report "$WORK/parallel-model-pulse-axis-support-probe.json" \
 --out "$WORK/parallel-model-pulse-weighted-axis-support.json"
```

加权支持引理使用 $A_\beta$ 的SPD流，作用于同一个欧氏曲面上的向量场；本条没有对G做各向异性的仿射变形。即使将来全前缀加权支持被认证，真实闭尾/帽/接缝、共同中心的完整闭面支持、实际完整曲率和D仍要分别支付，才能调用R650的reach结论。新全域支持计划将固定β1/4、Q8192/每片4径向子胞，并完整复用原819片λ预算；本条完成时尚未执行全域支持；后续五代表及固定全域批已另行启动，独立登记，不改本条有限点范围。
