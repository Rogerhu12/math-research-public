# 完整XYZ+87 log-radius新g设计首真步及目标曲率预算

## 1. 明确的新g设计身份

本条从实际G10选中zero6位置场、87个alpha全零起算，全部12789 XYZ方向和全部87个完整C2 log-radius方向共同进入真实12876列/4291840行求解。位置source独立于alpha，目标变为

\[
a_\alpha=a_0\exp h,\qquad h=\sum_{i=1}^{87}B_i\alpha_i.
\]

全部物理weights、source、端口和位置recipe固定；metric增益及q2面积对a的导数、全部XYZ/radius正规跨块真实保留。alpha的H2只作原增量阻尼，没有暗加绝对h惩罚或目标曲率项。**alpha变化明确改变g；本条计为新g设计接受，绝不计成原固定g改善或同g收敛。**

原首次大场FD短扫描自然exit1已独立登记；新数值consumer保持原算子/门槛，只把真实裸系数差分检查拓到1e−9。该大场实际检查相对FD1.71456796546e−8、adjoint9.39593209191e−15，之后才开始本条完整normal。

## 2. 全12876列实际normal与非线性接受

λ=1e−4，全部完整normal实际组装。XYZ/radius交叉块Frobenius范数72.2815173981，radius块2.25250674653，标量half bandwidth887；不是小核或对角近似。真实独立物理normal相对残差4.67573352181e−15，无需迭代修正。slope=−9.39087650412，全步预测下降9.39116513785，完整实际非线性长度1接受。

| 有限G10指标 | alpha=0基线 | 新g设计第1态 |
|---|---:|---:|
| R14² | 9.491143500485906 | 2.8213951569423905 |
| metric峰 | 1.321552140757598 | 1.5951072356069562 |
| own-curvature峰 | 2074.1505900159 | 711.5980234983732 |
| min sigma | 0.4715358740887159 | 0.5785521747622492 |
| min held | 0.6982203551991852 | 0.660345224779596 |
| area R² | 4.017106523988235e−7 | 0 |
| alpha infinity norm | 0 | 0.056460664242215436 |

本设计epoch自身新尝试/接受1/1，下一λ仍1e−4。state保完整12789位置系数、87alpha及其精确binary64 hex、物理knots、原g身份、源端口所有六jets/目标两jets、完整provisional metric定义。最终g尚未冻结；后续必须冻结alpha再真正做同g空间/网格加密。

solve自然exit0、外部522.052964449秒、child RSS602968KiB。完整联合normal段493.310260975秒，其中原XYZ完整band的角收缩434.033549409秒；删掉的是已无消费者的unscaled normal副本91471104字节，完整行列/全部跨块保持。

## 3. 同一新g的独立G11观察

668径点×256错移角、540个径点不在G10训练中；同一保存alpha在独立径点直接评价a0 exp(h)，没有另拟合g。新场G11metric=1.59806145083998、κ711.8648971646023、σ.5969138860147024。独立source直接六jets和修正直接三角评价保留，不参与试步选择。

该观察自然exit0、3.054872364秒、RSS114008KiB。所有metric、κ、σ和held仍是有限数值，没有连续sup或reach证书。

## 4. 新目标自身曲率必须另外支付

新增 `2ecf-polar-log-radius-target-audit.py` 从保存的alpha与原独立a0两jet计算

\[
K_\alpha=-a_\alpha''/a_\alpha
=K_0-2(a_0'/a_0)h'-h''-(h')^2.
\]

仅诊断，不改位置场/参数、接受判据或原14行。原g的G10/G11最大样本|K|分别6.08297474494/6.08224372269；新目标提高到48.1454508853/48.0492466467，最大为负K，G10位置s=.13800011636399237。两种公式实际差≤7.10542735761e−15。

这种变化说明不能仅看alpha幅度约.056或设计成本下降就称目标仍有原曲率资格。即使将来在该新g上找到准确等距嵌入，也还需要按该g与整个曲面的真实几何付reach条件。当前高|K|样本只是目标实际值，没有据此宣称障碍或连续极值。

脚本另外把保存alpha和物理knots解释为准确二进有理数，反复用准确B-spline差分公式求h的0至3阶控制数，并用非负partition-of-unity的convex hull覆盖每个完整span和两侧knot极限。结果：

| 全域标量h导数 | 准确有理上界的十进制展示 |
|---|---:|
| h绝对值 | 0.056460664242215436 |
| h一阶绝对值 | 0.6516712322161777 |
| h二阶绝对值 | 82.77168065764053 |
| h三阶绝对值分片两侧 | 82974.0909818109 |

JSON保所有准确分数，上表小数仅展示。a_alpha/a0的全域上下界保为exp(准确h控制数下/上界)符号式，没有把舍入exp冒成向外严格界。h,h',h''两端准确为零，内部knot重数≤3保证C2；源端口目标两jet保持。

这些准确界只覆盖h；未补原a0/a0'/a0''的连续区间，因此**没有声称连续K目标证界**。本新目标审计自然exit0、1.518335715秒、RSS89232KiB；第2个完整设计步已从该实际态继续。

## 5. 可复现入口与身份

完整G10 source/四基线按已发布G10基线note第4节。初始设计消费其同一zero6 baseline，命令如下（新输出prefix，不复写旧文件）：

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fd-step01" -- \
  python3 -u "$W/2ecf-polar-log-radius-streamed-fd-design-solve.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --warm-state "$W/polar-G10s-baseline-zero06-initial.json" --prefix "$W/polar-design-G10s-fd-step01" --steps 1
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fd-step01-target-audit" -- \
  python3 -u "$W/2ecf-polar-log-radius-target-audit.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --state "$W/polar-design-G10s-fd-step01-step01-state.json" \
  --observer "$W/polar-independent-G11r-shifted256-independent.json" \
  --output "$W/polar-design-G10s-fd-step01-target-audit.json"
```

G11观察沿用公开独立入口observe，将state设为同一新设计state；消费者会按其明确design schema读取保存alpha并核对provisional metric SHA。继续设计用同一入口的 `--state`，不再用 `--warm-state`重置alpha或次数。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-log-radius-streamed-fd-design-solve.py` | `21a8766d2d3ef8038ee821e03077b8d43ba852e35702fc10725f647a396f993b` |
| `2ecf-polar-log-radius-operator.py` | `f44226464ba3cad0f2c69f7bd9b7d86befa9a311d7ec268e0d81e7a19f36b17c` |
| `2ecf-polar-log-radius-target-audit.py` | `71a25dfbc7f2092f26f5f428442b4120ad0f39a2d826261490893c0db9a6008b` |
| `polar-design-G10s-fd-step01-step01-state.json` | `c1a8aae8acf9b3145e5b867bb4dbb7678f0f8a7a76035bc00d2081b4ee10f6fb` |
| `polar-design-G10s-fd-step01-exit.json` | `a82a386d358190d96e08def57bbba8046eb464f9a3395678a64fb2ac9323d1bd` |
| `polar-G11r-design-G10s-fd-step01.json` | `603f34c49b4172a3998bbd8695a88b9c6e4b311eb90b4bbb94daf5b97dbabd44` |
| `polar-G11r-design-G10s-fd-step01-exit.json` | `6efcb4a877602cf743129e1183035e50b9fc5e4f51dc92289f8e261f7f643036` |
| `polar-G10s-original-target-audit.json` | `83edecef3a10904cfa6112960e831b1b5b3a23e8cae3b12a1126df37d2a435ac` |
| `polar-design-G10s-fd-step01-target-audit.json` | `cd02137f703f5f47485921e455a9bace849cc1610d1ec0f7056e97705b45eaff` |
| `polar-design-G10s-fd-step01-target-audit-exit.json` | `54631437798b1237b3c445d489c761be15d2ade115ce2e547bdcc58f8bc33dac` |
