# G10全span完整源、四个全目标实基线：真正选中zero6

完成两次旧source求值失败的显式恢复后，新G10s完整source已真实生成并经过自然进程门；随后独立支付四个新有限目标baseline。新4291840行完整目标选中旧zero6，不是此前G3选择成本的warm3。所有本条baseline的新接受/尝试均为0；原同g首步已从该实际新baseline继续。

## 1. 完整数据，所有失败成本保留

目标径点集合为原205点、全部原G3径点、54个非空span各完整G10及各break的并集，共958径点，角维仍128与192，306560物理点，每点原13行+q2面积行，共 **4291840行、12789列**。每个span实际至少15个内部点。原g、原position source数学公式、物理位置与全C2空间保持；有限权重重付，原205成本不等同于本目标。

最终training组逐字采纳已完整exit0的G10r958×128源。observer新source采用已逐行flush完成的502行，实际再次重采索引0/251/501验证六jet与独立radius字节；余251行分成两个不相交实进程。原205 source六jet与radius在两组都逐字保持。

| 实际进程 | OS exit | 外部秒 | peak child RSS KiB |
|---|---:|---:|---:|
| G10r training恢复完整组 | 0 | 352.484388602 | 242220 |
| G10s observer[502,610)，108新行 | 0 | 447.454515217 | 242272 |
| G10s observer[610,753)，143新行 | 0 | 505.688548380 | 223608 |
| 新完整merge/assemble及恢复前缀实核 | 0 | 11.631168539 | 198100 |

两个observer chunk均实际遇到各自的原inverse门失败点，使用新一致arc reference审计，原位最大角残差7.6516484121e−15及7.6215075917e−15，外层5e−14保持。每个chunk的实际target oracle自然exit0。此前G10原128源exit1/1294.517秒及G10r192源exit1/1302.393秒仍独立留存，不能抵消、删除或当成接受。

完整prepared `polar-c2-G10s-prepared.json` SHA：

`de75e9632855bc3547e174d7e1bfcefaa295d01dbe151d1c087ff0d83682df80`

该prepared绑定完整旧/new source及原位恢复回执、原父prepared、全物理basis、实际quadrat权重和新consumer SHA；没有半组数据或虚构完整exit。

## 2. 四个完整新baseline

用已实际审计r/J/JT/S字节相等的完整分块重算入口，保全部行、角和原H2。每个候选先复制全部12789实际系数（literal zero为显式全零），独立记录新baseline/进程自然退出，新尝试和接受计数均归零。旧warm/zero次数仅作为来源计数，绝不借为G10新接受。

| 不变位置场输入 | 新G10 R14² | metric峰 | own-curvature峰 | min sigma | area R² |
|---|---:|---:|---:|---:|---:|
| warm03 | 11.0065766946 | 2.87944000142 | 723.068333304 | 0.467264908689 | 9.2065959e-07 |
| warm02 | 15.9815876655 | 1.8029495803 | 2348.50789685 | 0.283718759861 | 0.000411670248 |
| zero06 | 9.49114350049 | 1.32155214076 | 2074.15059002 | 0.471535874089 | 4.01710652e-07 |
| zero00 | 97.0910808749 | 0.939688020792 | 106.147088403 | 0.246013355676 | 0.209909044 |

新规则为最小 **本G10完整原14行R²**，因此选择zero6：R²=9.491143500485906，持有距离有限最小值.6982203551991852。此前G3选择专用成本在不同点/权重上将warm3排第一，实际G10四基线显示该排名不能借用；本次确实改选zero6，保其全系数场而不筛列。

所有metric/κ/sigma/held仍为有限点数值，不是连续上界或reach证书。此处选择成本也不是证误差趋于0。完整固定g真步从该状态起算新接受0→1，不继承G2 zero6的6次历史接受。

## 3. 实际baseline进程和完整身份

| 候选 | 自然exit | 外部秒 | baseline SHA256 |
|---|---:|---:|---|
| warm03 | 0 | 2.561833831 | `b7b85ec252820657821ff3e6cc19752cabeb19810ea82370d4178ce30752e169` |
| warm02 | 0 | 2.283070859 | `52acac3df1562415615f31f695ee88440738fe180b7b002b01563869eabd7e84` |
| zero06 | 0 | 2.640435694 | `4e71b271c603e08f6a838d0f70f92cbe00f1734c125b1f16ed4a756aa1611579` |
| zero00 | 0 | 2.323553785 | `b90238857487315e1e4092fb2c70f81bc5c4571c200e5b01488438b7bf680351` |

这些callback进程的父wrapper RSS为其到该时刻子进程峰值（cumulative maximum），各回执明确标识，不能把198100KiB当每个baseline的单独严格RSS。

完整选择receipt `polar-G10s-actual-baseline-selection.json` SHA：

`83ce7deedb2ac777037cd1a18380752f698ee0d47739c0f07c4ad955088d534a`

真正被选baseline SHA：

`4e71b271c603e08f6a838d0f70f92cbe00f1734c125b1f16ed4a756aa1611579`

原zero6系数态SHA：

`3faa387496334e0561982c1fc1e8723e889bdbef0fc88250847d460aff08868b`

## 4. 可变工作根下的完整新增流水命令

本节以已发布的原source/205点prepared和原G3独立cache为输入。它们的完整来源是 `2ecf-polar-full-prefix-warm-hidden-peaks` 第4节与 `2ecf-polar-independent-third-observer-reveals-prefix-peaks` 的公开source命令；原warm03/warm02/zero06由对应完整LM入口按其真实步序重生。以下只重生本条G10新增生产链，所有程序来自公开 `scripts`，不依赖写死路径的临时driver。prepared带绝对路径和本地回执，换工作根后的JSON SHA自然不同，源数组/数学参数的哈希和严格绑定检查仍生效。

首先设置三个绝对路径，`W`取保存上述输入的工作根。`S`是当前公开topic的scripts目录。为使 `Path(__file__).with_name(...)` 的已冻结依赖解析一致，把公开本次入口按原文件名复制到该工作根；不会修改仓库source。

```bash
TOPIC=/absolute/path/math-research-public/topics/visible-flexible-closed-surface
S="$TOPIC/scripts"
W=/absolute/path/reproduction-work
for entry in "$S"/2ecf-polar-*.py; do
  cp "$entry" "$W/"
done
base=(--scripts "$S" --parent-prepared "$W/polar-c2-extended-prepared.json"
  --third-observer "$W/polar-independent-G3-shifted256-independent.json"
  --candidate "$TOPIC/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json"
  --target-definition "$W/target-zero.json"
  --ramp-master "$W/gap105-prefix-ramp-master.npz"
  --coast-master "$W/gap105-prefix-coast-master.npz")
receipt="$W/2ecf-polar-natural-process-receipt.py"
```

为准确复现本条**失败后复用**身份，先实际执行两个旧消费者并记录其真实失败；不能手工造665或502行回执。可移植 `2ecf-polar-natural-process-receipt.py` 把实际命令、自然退出码、时间/RSS和日志写入 `PREFIX-exit.json` / `PREFIX.log`；expected-returncode只检查退出，不改变子进程。若不同数值平台的实际失败点/行数不同，当前恢复入口会拒绝，需要另立真实consumer，不能改回执迁就本条。

```bash
python3 "$receipt" --prefix "$W/polar-c2-G10-training-source" --expected-returncode 1 -- \
  python3 -u "$W/2ecf-polar-c2-g10-prepare.py" cache "${base[@]}" \
  --prefix "$W/polar-c2-G10" --group training
python3 "$receipt" --prefix "$W/polar-c2-G10r-training-source" -- \
  python3 -u "$W/2ecf-polar-c2-g10-resume-prepare.py" cache "${base[@]}" \
  --prefix "$W/polar-c2-G10r" --group training --failed-prefix "$W/polar-c2-G10"
python3 "$receipt" --prefix "$W/polar-c2-G10r-observer-source" --expected-returncode 1 -- \
  python3 -u "$W/2ecf-polar-c2-g10-resume-prepare.py" cache "${base[@]}" \
  --prefix "$W/polar-c2-G10r" --group observer
python3 "$receipt" --prefix "$W/polar-c2-G10s-chunk502-610-source" -- \
  python3 -u "$W/2ecf-polar-c2-g10-split-prepare.py" cache "${base[@]}" \
  --prefix "$W/polar-c2-G10s-chunk502-610" --group observer --first 502 --stop 610
python3 "$receipt" --prefix "$W/polar-c2-G10s-chunk610-753-source" -- \
  python3 -u "$W/2ecf-polar-c2-g10-split-prepare.py" cache "${base[@]}" \
  --prefix "$W/polar-c2-G10s-chunk610-753" --group observer --first 610 --stop 753
python3 "$receipt" --prefix "$W/polar-c2-G10s-assemble" -- \
  python3 -u "$W/2ecf-polar-c2-g10-split-prepare.py" assemble "${base[@]}" \
  --prefix "$W/polar-c2-G10s" --completed-training-prefix "$W/polar-c2-G10r-training" \
  --failed-observer-prefix "$W/polar-c2-G10r-observer" \
  --chunk-prefixes "$W/polar-c2-G10s-chunk502-610" "$W/polar-c2-G10s-chunk610-753"
```

新helper `longdouble_primitive` 内继承的旧docstring仍提及 frozen anchors/normalization，**这段历史docstring已经不描述新reference实现**。新实际reference由冻结Fourier重新积分累计并重算derived raw.a/normalization；原物理半径和独立g固定，生产source不写回reference。以具体实现、G16/G32实际回执和前一条一致arc审计为准。为保活动source及所有哈希身份，此时不就地改该docstring。

然后每个候选真实支付完整新目标，再选择最小R²。代码只在四进程自然0且初态计数全0后排序；不从旧G3成本排序。

```bash
solve=(python3 -u "$W/2ecf-polar-c2-g10-solve.py" --scripts "$S"
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py"
  --prepared "$W/polar-c2-G10s-prepared.json")
for label in warm03 warm02 zero06 zero00; do
  case "$label" in
    warm03) parent=(--warm-state "$W/polar-c2-step03-step01-state.json") ;;
    warm02) parent=(--warm-state "$W/polar-c2-step02-step01-state.json") ;;
    zero06) parent=(--warm-state "$W/polar-c2-zero-step06-step01-state.json") ;;
    zero00) parent=(--zero) ;;
  esac
  python3 "$receipt" --prefix "$W/polar-G10s-baseline-$label" -- \
    "${solve[@]}" "${parent[@]}" --prefix "$W/polar-G10s-baseline-$label" --steps 0
done
python3 - "$W" <<'PYSELECT'
from pathlib import Path
import json,sys
w=Path(sys.argv[1]);values=[]
for label in ('warm03','warm02','zero06','zero00'):
    p=w/('polar-G10s-baseline-'+label+'-initial.json')
    row=json.loads(p.read_text())
    receipt=json.loads((w/('polar-G10s-baseline-'+label+'-exit.json')).read_text())
    assert receipt['returncode']==0
    assert row['ownExtendedAcceptedSteps']==row['ownExtendedAttempts']==0
    values.append((row['evaluation']['squaredNorm'],label,str(p)))
best=min(values)
(w/'actual-G10-selection-for-reproduction.json').write_text(json.dumps(dict(all=values,selected=best)))
(w/'actual-G10-selected-state.txt').write_text(best[2]+'\n')
print(best)
PYSELECT
read -r chosen < "$W/actual-G10-selected-state.txt"
python3 "$receipt" --prefix "$W/polar-G10s-step01" -- \
  "${solve[@]}" --state "$chosen" --prefix "$W/polar-G10s-step01" --steps 1
python3 "$receipt" --prefix "$W/polar-G11r-G10s-step01" -- \
  python3 -u "$W/2ecf-polar-c2-independent-g11-resume-observe.py" observe \
  --scripts "$S" --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" \
  --prepared "$W/polar-c2-G10s-prepared.json" --state "$W/polar-G10s-step01-step01-state.json" \
  --observer "$W/polar-independent-G11r-shifted256-independent.json" \
  --output "$W/polar-G11r-G10s-step01.json"
```

G11完整独立source先按 `2ecf-polar-G11-source-failure-and-433-row-recovery` 的公开命令生成。此条仅登记完整source和四baseline；末尾两条首步/观察命令是实际继续入口，结果单独按其自然退出登记。新g设计支从选中父态、alpha=0起算，所有87 alpha改变另算新g设计，不混入该固定g链。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-c2-g10-split-prepare.py` | `fe7946d5b0156dcc507ee10bb387080179af5269ceb004e6c7630ff80279e04b` |
| `2ecf-polar-refined-arc-source-evaluator.py` | `fa33a49b999b5266da9faffc6f4eb8fece36539f71d10f6a8ee39ba0ba893f5b` |
| `2ecf-polar-G10-split-actual-first-step-driver.py` | `8fac52c2b4caff42255cef3d9ad9bb5a32149101512b27732eaf6afdeddd214f` |
| `2ecf-polar-c2-g10-solve.py` | `baad827f707e889f1be395d7b010dc91c1f39ce21bebdd5042e992038ffce642` |
| `2ecf-polar-complete-two-grid-streamed.py` | `013af2fb811c6d74ab58f69d8ade9c52e767d5dc2bef212b9eff900cb6e1d475` |
| `polar-c2-G10s-training-group.json` | `91497b3116f0f4a7320f49ac8710f9eb7fa28481acfc1fb0f8db76f21893b044` |
| `polar-c2-G10s-observer-group.json` | `e2f18b84e804e550eb28bafe5d85533748ae918782919345e14933fcc09ce446` |
| `polar-c2-G10s-observer-jets.npy` | `09f64bfc03575c160c4851313ea8c2993591ee2523b648f8c1851ebbcdc29c9b` |
| `polar-c2-G10s-observer-radius.npy` | `3c22996d7fdc63ded582b2c291dceafd357c7244587d4d908d164c2dfe1b17e5` |
| `polar-c2-G10s-assemble-exit.json` | `439f2524d5bfc83ca84e3efd399a9d7a182ee254f9e3bf91aa2a42885d1299cf` |
| `polar-c2-G10s-chunk502-610-source-exit.json` | `f5cb76508f3fd9a7aa8a65cd10450e8eec874e2fe1e47268c49dc4928d358d3d` |
| `polar-c2-G10s-chunk610-753-source-exit.json` | `31aa586ce53f165bdeb7dc8799d6330b526b502e577b9bdd70f58b1fcc156d40` |

本条只有source完成和四个新实基线/实际父态选择；不冒新LM接受、连续解、whole closed或全时reach。

可移植自然退出记录器 `2ecf-polar-natural-process-receipt.py` SHA256 `fd62a0f5e3d09b6d7ee024ce03219bbaab3a6a9cc728573b35d31d4af58384cb`；负返回码按真实signal单列，不能标为natural exit。既有实际0/1记录不改。
