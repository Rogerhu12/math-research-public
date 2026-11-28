# 全G10完整normal的稀疏jet角收缩与真实JᵀJ审计

## 1. 不减少任何物理行列的代数重排

原完整normal在每个实际径点先形成所有14行对6个三维position jets的Gram C，再通过全部有符号Fourier矩得到角通道的完整正规耦合。G10首步实测角收缩297秒，占normal主成本；原例程为每对Cartesian分量保存四个完整6×6 complex moment再与多零矩阵相乘。

新核 `2ecf-polar-complete-sparse-jet-angular.py` 直接展开同一6个非零jet槽。对一个角通道p及径向导数d，其jet角系数是

\[
T_0(p)=(p,0,p',0,0,p''),\quad
T_1(p)=(0,p,0,0,p',0),\quad
T_2(p)=(0,0,0,p,0,0).
\]

这里jet顺序为X,Xs,Xu,Xss,Xsu,Xuu。p按原cos/sin的全部正负指数两槽展开，每阶角导数乘(ik)^j；对每一对通道、每一对Cartesian分量、每个d/e、每个实际非零jet对，累加原

\[
\sum_u C_{ab}^{ij}(u)T_d(p)_iT_e(q)_j.
\]

每项仍由完整离散rFFT正指数矩得到，频率按N取模，正半谱用conjugate、负/alias用已存半谱；常数cos只保其真实单槽。没有FFT截断、去掉cross channel、丢弃残差行或角点。对准确实数算术，这正是原完整normal的有限求和分配律展开；浮点求和顺序改变，故另有consumer与实际误差审计，不宣称逐字相等。

## 2. 六个真实非零G10 block的直接原式比较

取实际G10第1态，原source/target/weights，128角和192角两组各取第1/10/60号完整径向block，每block12径点、所有147角通道与全部14行Gram。新旧完整Q的相对Frobenius差依次：

- 128角：1.59133e−16、1.52480e−16、1.55347e−16；
- 192角：1.62876e−16、1.50738e−16、1.61085e−16。

最大逐元素绝对差3.55271367880e−15。六例旧角核累计21.363181115秒，新核6.974614107秒；这是本次实际基准，不保证任意硬件相同比例。当前M24和N128/192无alias频对；代码数学规则保留alias，并不把零alias实际例假报成已执行alias案例。

此审计自然exit0、37.333937975秒、RSS464128KiB。只核完整角收缩，不计优化接受。

## 3. 真实全4291840行、12789列normal核

静态新模块 `2ecf-polar-complete-sparse-jet-normal.py` 从已冻结原完整normal模块复制，唯一算法替换是上述角收缩。原完整point covariance、全部径向累积、全部Cartesian跨分量、原H2、对角等价缩放和band Cholesky均保留；receipt写明原模块及新核SHA。

真正采用G10第2态、λ=1.1111111111111112e−5，全部958×(128+192)点的原13+q2行、全部12789列完整组装。构造的band实际全维求解后，再用原完整point J/JT从头评价物理normal残差，**不使用刚组装band来检查自己**：

| 全规模核对 | 实际相对误差 |
|---|---:|
| 完整物理normal方程 | 1.46970869636e−14 |
| 完整band对独立JᵀJ，裸全系数探针 | 1.67480013223e−15 |
| 完整band对独立JᵀJ，Sobolev全系数探针 | 2.98436573996e−14 |

全normal实际组装112.051240610秒，其中point covariance10.620秒、angular75.530秒、radial24.256秒。原固定g第3步恰从同一第2态和同一λ组装原normal，实际assembly346.454672947秒、angular312.810025677秒，物理normal残差1.47977656208e−14。两实进程并行调度环境不完全隔离，故记录实时间而不许诺普适加速比例。

全规模审计自然exit0、外部139.455890340秒、RSS514992KiB。没有非线性试步或接受。新receipt的largestTrackedOuterTemporaryBytes只追踪外层临时数组，明确不含稀疏角核内部临时，不将它冒成总内存或RSS。

## 4. 显式实现迁移，不借旧次数

新设计入口 `2ecf-polar-log-radius-fast-normal-design-solve.py` 保旧FD设计入口的全部物理目标、source、target参数定义、点/权重、H2、接受规则和完整联合算子，只装载新完整normal核。消费者必须读取本实际全G10 normal审计并核prepared/行列/normal SHA。

从旧FD入口接续时，逐字段检查旧model与新model只差明确normal实现及solver SHA字段；新消费者实际重付完整baseline和每组统计，并要求与保存旧state逐值相同。实现历史保存旧state/model/solver SHA、新solver SHA、真实旧次数和此实现迁移新尝试0；不将旧接受再报一遍。随后每个真正新步仍重新支付全12876列normal与原physical residual门。

在真实非零alpha设计第1态上，已实际执行 `--steps 0` 的迁移消费：全部baseline/group values相同，所有12789+87保存参数相同，继承设计接受1但本进程新接受0；自然exit0。它仅验证迁移身份，尚非新fast nonlinear步。当前旧科学进程保持不动，下一设计步自然结束后再用独立新consumer继续并分别登记新实步。

## 5. 可复生命令与身份

W/S及完整prepared见G10完整baseline note。先执行小型角核比较，再执行全G10 normal审计：

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-G10s-sparse-jet-angular-audit" -- \
  python3 -u "$W/2ecf-polar-complete-sparse-jet-angular-audit.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --state "$W/polar-G10s-step01-step01-state.json" --output "$W/polar-G10s-sparse-jet-angular-audit.json"
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-G10s-sparse-jet-full-normal-audit" -- \
  python3 -u "$W/2ecf-polar-complete-sparse-jet-normal-audit.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --state "$W/polar-G10s-step02-step01-state.json" --output "$W/polar-G10s-sparse-jet-full-normal-audit.json"
```

完整新设计消费用 `2ecf-polar-log-radius-fast-normal-design-solve.py`，添加 `--normal-audit "$W/polar-G10s-sparse-jet-full-normal-audit.json"`；其余使用原设计入口同一prepared/state/steps约定。0步迁移检查和后续真步都必须选新prefix。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-complete-sparse-jet-angular.py` | `79735d9dcdbc37dec7de70f7ac7bd16dfd766621ca18187cb7816356683e4ddb` |
| `2ecf-polar-complete-sparse-jet-angular-audit.py` | `78608e332f60b649f45457427f4a060a687f8a698e9a56cf74fbe2898be9bfe9` |
| `polar-G10s-sparse-jet-angular-audit.json` | `adea56eb13ede591c484cc3c036221b162a46390ad60b05cae329faeb434c0cb` |
| `polar-G10s-sparse-jet-angular-audit-exit.json` | `db2005a64cae650b4c6e03543de44f06e472228517b0e94d3be530c2da6f58e7` |
| `2ecf-polar-complete-sparse-jet-normal.py` | `4c81e117e977f9a80252f1edc6b2cc270ef8b8575e1bd45c4eda1f0c8d09367b` |
| `2ecf-polar-complete-sparse-jet-normal-audit.py` | `bc2d4b8f4998bc64c4a533fa54cc9558d462bcb586859bbaaf2d696a77e578f5` |
| `polar-G10s-sparse-jet-full-normal-audit.json` | `62fb3e1f411ddcfc98c8e4ccefb9afeb82b5fdca6c3a2de44d4d7cb088e23b66` |
| `polar-G10s-sparse-jet-full-normal-audit-exit.json` | `9505856bd06cb5357aff54820921a192992cef14c96747ba53c577aefa2b7be8` |
| `2ecf-polar-log-radius-fast-normal-design-solve.py` | `21ce120289efa4f35decd7e7de120d501fa4392cb9bb4deb6c562e656662ea3d` |
| `polar-design-G10s-fast-transition-audit-initial.json` | `45cf2b27fe599c566465155a6264bc4f722dc08493c263b087d04ccbd509d77f` |
| `polar-design-G10s-fast-transition-audit-exit.json` | `6c979ed1ae876fc703520b36b9b4adf1b7c4d8f70553d66ee53597f27cf936d4` |
