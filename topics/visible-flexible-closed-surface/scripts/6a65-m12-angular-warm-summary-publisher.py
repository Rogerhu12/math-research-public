#!/usr/bin/env python3
"""Publish one small actual-conclusion note; complete outputs stay RUNNER_TEMP.

The numerical source is frozen elsewhere. Only an explicitly identified,
unpublished one-commit note may be dropped after an ordinary NFF rejection.
Every subsequent literal pull is handled by the shared live-rules monitor,
which records a changed README in HANDOFF before stopping with exit 42.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path

TOPIC=Path('topics/visible-flexible-closed-surface')
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda:source.read(1048576),b''):h.update(block)
    return h.hexdigest()
def read(path):return json.loads(path.read_text()) if path.exists() else None
def cell(value):
    if value is None:return 'missing'
    if isinstance(value,bool):return 'true' if value else 'false'
    if isinstance(value,float):return format(value,'.17g')
    return str(value).replace('|','/').replace('\n',' ')
def get(value,*keys):
    for key in keys:
        if not isinstance(value,dict):return None
        value=value.get(key)
    return value
def display(value):
    if not isinstance(value,dict):return value
    return value.get('display',value.get('upper_display',value.get('upper_numerical')))

def make_summary(args):
    cold=args.directory;task=cold/'entire-half';base=task/'h487-base'
    observed=read(task/'entire-half-result.json') or {}
    base_observed=read(base/'entire-half-result.json') or {}
    warm_observed=read(task/'entire-half-result.json.warm-observed.json') or {}
    supervised=read(cold/'supervised-execution.json') or {}
    rules=read(cold/'live-rules-checks.json') or {}
    execution=read(task/'entire-half-cold-execution.json') or {}
    base_execution=read(base/'entire-half-cold-execution.json') or {}
    transfer=read(task/'entire-half-warm-transfer.json') or {}
    def report(directory,name):return read(directory/('entire-half-'+name+'.json')) or {}
    metric=report(task,'localized-metric-budget');base_metric=report(base,'localized-metric-budget')
    geometry=report(task,'actual-field-geometry');meshes=report(task,'closed-stl')
    final_micro=report(task,'original-span-observer');warm_micro=report(task,'warm-original-span-observer')
    final_union=report(task,'old-observer-union');warm_union=report(task,'warm-old-observer-union')
    for label,field,budget in [('M48',observed,metric),('same-job h487',base_observed,base_metric)]:
        if budget and (not field or any(budget.get(k)!=field.get(k) for k in ('field_sha256','grid_sha256'))):
            raise ValueError(label+' continuous bound does not consume its actual field/grid')
    if supervised.get('rules_changed') or rules.get('rules_changed'):
        raise RuntimeError('README changed: numerical conclusion publication is forbidden')
    out=['# 原 M12 同 g：h487 重生到 M48 的实际暖续摘要','',
        '**可信度：实际有限数值结果及本次连续验证器的条件结论。没有证明精确等距，也没有宣称课题完成。**','',
        '- Run: `'+args.run_id+'`，attempt `'+args.attempt+'`；冻结源 `'+args.source_head+'`。',
        '- Actions: https://github.com/Rogerhu12/math-research-public/actions/runs/'+args.run_id,
        '- 完整范围：原固定 g 的中央、prefix、bridge、有限尾和真实平 cuff；全部内部接口联动。',
        '- 基态重生：80/64/depth12、原元 190/176 的 h487、M32/N384/G6、800 LSMR、1 Newton、block24。重生本身不算新下降。',
        '- 暖续：相同径向节点、G6 和精确 query；M48/N768、LSMR '+os.environ.get('M12_WARM_ITERATIONS','missing')+
        '、Newton '+os.environ.get('M12_WARM_NEWTON','missing')+'；实际同 job 基态完整系数零填充，lambda=0。',
        '- 独立观察：G8/N1536，双原始 span 微窗及全部祖先点保留；基态旧观察为 G8/N768。',
        '- 执行入口：`scripts/6a65-m12-h487-to-m48-angular-warm-cold-run.py`；request `ci-requests/6a65-m12-h487-angular-warm.json`。',
        '- 全部报告、证书、原始场、mesh 与日志只留 RUNNER_TEMP / Actions logs；下列为结论引用，完整报告没有分件入库。','',
        '## 实际执行与场身份','',
        '| 项目 | 实际值 |','|---|---|']
    identities=[('publication 前 job 状态',args.job_status),('supervisor 完整结束',supervised.get('finished')),
        ('暖续冷入口完整结束',execution.get('finished')),('基态入口完整结束',base_execution.get('finished')),
        ('supervisor 秒数',supervised.get('seconds')),('暖续实际使用输入场而未清零',observed.get('actual_warm_field_used_without_reset')),
        ('本层接受步数',observed.get('accepted_steps_this_refinement')),('基态 field',base_observed.get('field_sha256')),
        ('基态 grid',base_observed.get('grid_sha256')),('暖初场 field',warm_observed.get('field_sha256')),
        ('新场 field',observed.get('field_sha256')),('新场 grid',observed.get('grid_sha256')),
        ('新层元素',observed.get('elements')),('新层未知数',observed.get('unknowns')),
        ('J/JT 相对误差',observed.get('analytic_adjoint_relative_error')),
        ('中央及真实 cuff 修正两 jets 最大值',observed.get('central_and_true_cuff_correction_jets_max')),
        ('实际完整峰位 q',observed.get('independent_peak_material_q')),
        ('实际 RSS high-water KiB',observed.get('resident_high_water_KiB')),
        ('规则拉取次数',len(rules.get('events',[]))),('最后规则读取 SHA',rules.get('last_rules_read_sha'))]
    for key,value in identities:out.append('| '+key+' | '+cell(value)+' |')
    out+=['','## 同场完整残差','',
          '| 场 / 观察 | metric 峰 | 加权能量 | curvature 峰 | support 下界 |',
          '|---|---:|---:|---:|---:|']
    for label,value in [('同 job h487 独立观察',base_observed.get('independent_observer_after')),
             ('M48 暖初场独立观察',observed.get('independent_observer_initial_warm_field')),
             ('M48 暖续后独立观察',observed.get('independent_observer_after')),
             ('暖初场祖先并集',warm_union.get('union_after')),('暖续后祖先并集',final_union.get('union_after'))]:
        out.append('| '+label+' | '+' | '.join(cell(get(value,k)) for k in ('metric_peak','weighted_energy','curvature_peak','support_lower'))+' |')
    out+=['','祖先并集的能量栏缺失是因为该集合没有统一求积权；不把两个不同角网格的峰差误称同点差。','',
          '| 相交原 span 微窗 | 暖初场峰 | 暖续后峰 | 新峰原 span |',
          '|---|---:|---:|---:|']
    old_windows={w['window_index']:w for w in warm_micro.get('window_observations',[])}
    for w in final_micro.get('window_observations',[]):
        initial=old_windows.get(w['window_index'],{})
        out.append('| '+cell(w.get('window_exact'))+' | '+cell(get(initial,'after','metric_peak'))+' | '+
                   cell(get(w,'after','metric_peak'))+' | '+cell(get(w,'after','source_span'))+' |')
    out+=['','这些观察保留与名义窗口相交的完整原始 span 的四分点，不宣称最坏点必在名义窗口内。','',
          '| Newton 步 | LSMR stop / 迭代 | 接受 alpha | 真实物理正规残差比 | 完整方向 slope |',
          '|---:|---|---:|---:|---:|']
    for row in observed.get('rows',[]):
        d=row.get('actual_linear_solver_diagnostics',{})
        out.append('| '+cell(row.get('step'))+' | '+cell(row.get('lsmr_stop'))+' / '+cell(row.get('lsmr_iterations'))+
                   ' | '+cell(row.get('accepted_alpha'))+' | '+cell(d.get('actual_relative_physical_normal_norm'))+
                   ' | '+cell(d.get('actual_unregularized_direction_slope'))+' |')
    out+=['','stop 7 只表示达到迭代限额；有限采样小残差、非线性接受和完整连续界均不替代固定 g 精确解或 solver 收敛证明。','',
          '## 本次实际连续验证与网格','',
          '| 项目 | 实际值 |','|---|---|']
    checks=[('h487 R236 连续 metric 上界（显示值）',display(base_metric.get('metric_triangle_upper'))),
        ('新场 R236 连续 metric 上界（显示值）',display(metric.get('metric_triangle_upper'))),
        ('新场 R236 小于 1e-6',metric.get('continuous_metric_below_1e_6')),
        ('R236 保持同一场和同一 g',bool(metric and metric.get('same_actual_field_no_refit') and metric.get('same_original_exact_metric'))),
        ('全空间 / 全相位几何传递',geometry.get('homotopy_embedded_and_reach_transfer_proved')),
        ('reach/D 下界（显示值）',get(geometry,'rational_quantities','reach_over_diameter','display')),
        ('held/D 下界（显示值）',get(geometry,'rational_quantities','held_over_diameter','display')),
        ('全域曲率上界（显示值）',get(geometry,'rational_quantities','actual_principal_curvature','display')),
        ('非全等三阶实矩条件',get(geometry,'checks','activity_real_third_moment_positive')),
        ('全祖先观察集合包含',final_union.get('union_contains_all_recorded_ancestor_observers')),
        ('完整三相位 STL 个数',len(meshes.get('meshFiles',[]))),
        ('STL 固定帽字节相同',meshes.get('fixedCapsBitwiseIdenticalInSerializedFloat32')),
        ('STL Euler 特征',get(meshes,'topology','EulerCharacteristic')),
        ('STL 每边两次相反关联',get(meshes,'topology','allEdgesHaveTwoOppositeIncidences'))]
    for key,value in checks:out.append('| '+key+' | '+cell(value)+' |')
    out+=['','严格方向由被哈希绑定的完整有理报告给定；这里的浮点显示值不当作重新向外取整的严格端点。全相位结论来自既有连续传递证明及本次条件检查，三张 STL 是有限网格。','',
          '## 实际阶段退出','',
          '| 阶段 | exit | 秒 |','|---|---:|---:|']
    for prefix,record in [('supervisor',supervised),('warm-entry',execution),('base-entry',base_execution)]:
        for stage in record.get('stages',[]):
            out.append('| '+prefix+': '+cell(stage.get('stage',stage.get('name')))+' | '+
                       cell(stage.get('exit_code',stage.get('returncode')))+' | '+cell(stage.get('seconds'))+' |')
    out+=['','## 完整输出 SHA-256','',
          '以下路径相对本 run 的 RUNNER_TEMP 工作目录；只登记身份，不把可重算内容提交到仓库。`cold-receipt.json` 还绑定恢复输入、缓存及全部原始输出；完整内容在 Actions logs / runner，可由上述冻结源与参数重生。','',
          '| 输出 | SHA-256 |','|---|---|']
    # Every complete JSON report is cited, alongside actual field/mesh files.
    # The receipt binds all other raw arrays and the original query inputs.
    for path in sorted(cold.rglob('*')):
        if not path.is_file():continue
        rel=str(path.relative_to(cold))
        if path.suffix=='.json' or path.name.endswith('.field.npz') or path.suffix=='.stl':
            out.append('| `'+rel+'` | `'+sha(path)+'` |')
    out+=['','无 complete report / certificate / Actions 输出入库；本 note 只给实际结论、参数、run 与输出身份。若某阶段缺失，上表保留 missing，不宣称该项完成。','']
    raw='\n'.join(out).encode('utf-8')
    if len(raw)>40000:raise ValueError('Actual-conclusion summary unexpectedly exceeds 40 KB')
    return raw

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('repository','frozen-root','directory'):ap.add_argument('--'+key,type=Path,required=True)
    for key in ('source-head','run-id','attempt','job-status'):ap.add_argument('--'+key,required=True)
    args=ap.parse_args()
    if args.repository.resolve()==args.frozen_root.resolve():raise ValueError('Publication worktree must be separate')
    supervisor=args.frozen_root/TOPIC/'scripts/6a65-m12-angular-warm-rules-supervisor.py'
    spec=importlib.util.spec_from_file_location('m12_rules_for_summary',supervisor)
    rules_module=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules_module)
    state_path=args.directory/'live-rules-checks.json'
    monitor=rules_module.RulesMonitor(args.repository,args.source_head,args.run_id,args.attempt,state_path)
    old=read(state_path)
    if old:
        monitor.last_read=old['last_rules_read_sha'];monitor.events=old.get('events',[])
        monitor.changed=bool(old.get('rules_changed'))
    if monitor.changed:
        print('README change was already recorded; no numerical note will be published',flush=True)
        raise SystemExit(42)
    target=TOPIC/'notes'/('2026-11-26-6a65-m12-angular-warm-ci-'+args.run_id+'-'+args.attempt+'.md')
    subject='Record M12 fixed-g angular warm conclusion run '+args.run_id+' attempt '+args.attempt
    while True:
        try:monitor.check_and_publish()
        except rules_module.RulesChanged as error:
            print(str(error),flush=True);raise SystemExit(42)
        raw=make_summary(args)
        (args.directory/'pending-actual-conclusion.md').write_bytes(raw)
        path=args.repository/target;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
        monitor.git('add','--',str(target))
        if monitor.git('diff','--cached','--quiet',check=False).returncode==0:
            print('Actual-conclusion note already present with identical bytes',flush=True);return
        parent=monitor.git('rev-parse','HEAD').stdout.strip()
        monitor.git('commit','-m',subject)
        own=monitor.git('rev-parse','HEAD').stdout.strip()
        push=monitor.git('push','origin','HEAD:main',check=False)
        if push.returncode==0:
            print(json.dumps({'published_actual_conclusion':str(target),'sha256':hashlib.sha256(raw).hexdigest(),
                              'bytes':len(raw),'commit':own,'complete_reports_published':False}),flush=True);return
        if not rules_module.concurrent_ref(push.stderr):
            raise RuntimeError('Ordinary conclusion push failed: '+push.stderr.strip())
        # Drop exactly this single unpublished note in this disposable worktree
        # before the next pull. A README change can then publish only HANDOFF,
        # never accidentally carry this unapproved-by-new-rules conclusion.
        if monitor.git('rev-parse','HEAD').stdout.strip()!=own:
            raise RuntimeError('Unexpected HEAD while withdrawing own unpublished note')
        parents=monitor.git('rev-list','--parents','-n','1',own).stdout.split()
        names=monitor.git('diff-tree','--no-commit-id','--name-only','-r',own).stdout.splitlines()
        if parents!=[own,parent] or names!=[str(target)] or monitor.git('log','-1','--format=%s').stdout.strip()!=subject:
            raise RuntimeError('Refusing to withdraw anything except own one-note unpublished commit')
        if monitor.git('status','--porcelain','--untracked-files=no').stdout.strip():
            raise RuntimeError('Unexpected tracked work; will not reset it')
        if monitor.git('merge-base','--is-ancestor',own,'origin/main',check=False).returncode==0:
            raise RuntimeError('Refusing to withdraw a commit already recorded upstream')
        monitor.git('reset','--hard',parent)
        # The next operation is literal pull --rebase with immediate README
        # diff, then the ordinary H-only/NFF loop. No remote force operation.

if __name__=='__main__':main()
